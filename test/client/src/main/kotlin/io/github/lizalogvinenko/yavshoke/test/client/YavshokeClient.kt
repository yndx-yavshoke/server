package io.github.lizalogvinenko.yavshoke.test.client

import io.github.lizalogvinenko.yavshoke.test.client.dto.exist.ExistRequest
import io.github.lizalogvinenko.yavshoke.test.client.dto.login.LoginRequest
import io.github.lizalogvinenko.yavshoke.test.client.dto.register.RegisterRequest
import io.github.lizalogvinenko.yavshoke.test.client.dto.update.UpdateRequest
import io.ktor.client.HttpClient
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.plugins.DefaultRequest
import io.ktor.client.plugins.contentnegotiation.ContentNegotiation
import io.ktor.client.plugins.logging.Logging
import io.ktor.client.request.bearerAuth
import io.ktor.client.request.get
import io.ktor.client.request.patch
import io.ktor.client.request.post
import io.ktor.client.request.setBody
import io.ktor.client.statement.HttpResponse
import io.ktor.http.ContentType
import io.ktor.http.contentType
import io.ktor.serialization.kotlinx.json.json

class YavshokeClient(private val client: HttpClient) {

    suspend fun register(request: RegisterRequest): HttpResponse {
        return client.post("/auth/register") {
            setBody(request)
        }
    }

    suspend fun login(request: LoginRequest): HttpResponse {
        return client.post("/auth/login") {
            setBody(request)
        }
    }

    suspend fun update(request: UpdateRequest, bearerToken: String): HttpResponse {
        return client.patch("/user/name") {
            setBody(request)
            bearerAuth(bearerToken)
        }
    }

    suspend fun exist(request: ExistRequest): HttpResponse {
        return client.post("/exist") {
            setBody(request)
        }
    }


    suspend fun getUser(bearerToken: String?): HttpResponse{
        return client.get("/user/me"){
            if (bearerToken != null) {
                bearerAuth(bearerToken)
            }
        }
    }

    companion object {
        const val DEFAULT_BASE_URL = "http://localhost:3000/"

        fun create(baseUrl: String = DEFAULT_BASE_URL): YavshokeClient {
            val client = HttpClient(OkHttp) {
                install(DefaultRequest) {
                    url(baseUrl)
                    contentType(ContentType.Application.Json)
                }
                install(ContentNegotiation) {
                    json()
                }
                install(Logging)
            }

            return YavshokeClient(client)
        }
    }
}