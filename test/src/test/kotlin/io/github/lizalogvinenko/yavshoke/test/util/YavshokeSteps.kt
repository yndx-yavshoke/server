package io.github.lizalogvinenko.yavshoke.test.util

import io.github.lizalogvinenko.yavshoke.test.client.YavshokeClient
import io.github.lizalogvinenko.yavshoke.test.client.dto.login.LoginRequest
import io.github.lizalogvinenko.yavshoke.test.client.dto.login.LoginResponse
import io.github.lizalogvinenko.yavshoke.test.client.dto.register.RegisterRequest
import io.ktor.client.call.body
import java.util.Base64
import java.util.UUID

class YavshokeSteps(private val client: YavshokeClient) {

    /**
     * @return bearer token for the newly created user
     */
    suspend fun createUserAndAuthenticate(age: Long = StubUser.AGE): AuthenticationResult {
        val email = "${randomString()}@yavshoke.ru"
        val password = randomString()

        client.register(
            RegisterRequest(
                email = email,
                password = password,
                age = age
            )
        )

        val loginResponse = client.login(
            LoginRequest(
                email = email,
                password = password
            )
        )

        return AuthenticationResult(
            email = email,
            token = loginResponse.body<LoginResponse>()
                .token
        )
    }

    private fun randomString(): String {
        val uuid = UUID.randomUUID().toString()
        return Base64.getEncoder().encode(uuid.toByteArray())
            .toString(Charsets.UTF_8)
            .substring(0, 20)
    }
}