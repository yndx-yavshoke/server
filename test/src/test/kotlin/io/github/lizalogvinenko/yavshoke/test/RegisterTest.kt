package io.github.lizalogvinenko.yavshoke.test

import io.github.lizalogvinenko.yavshoke.test.client.YavshokeClient
import io.github.lizalogvinenko.yavshoke.test.client.dto.register.RegisterRequest
import io.github.lizalogvinenko.yavshoke.test.client.dto.register.RegisterResponse
import io.github.lizalogvinenko.yavshoke.test.util.StubUser
import io.ktor.client.call.body
import io.ktor.http.HttpStatusCode
import kotlinx.coroutines.test.runTest
import org.junit.jupiter.api.Assertions
import java.util.Base64
import java.util.UUID
import kotlin.test.Test

class RegisterTest {
    val client = YavshokeClient.create()

    @Test
    fun `REGISTER user`() = runTest {
        val email = "${randomString()}@yavshoke.ru"
        val response = client.register(
            RegisterRequest(
                email = email,
                password = "12345678",
                age = StubUser.AGE
            )
        )

        Assertions.assertEquals(HttpStatusCode.OK, response.status)

        val body = response.body<RegisterResponse>()

        Assertions.assertEquals(
            RegisterResponse.User(
                id = body.user.id,
                email = email,
                name = body.user.name,
                age = StubUser.AGE
            ),
            body.user
        )

        Assertions.assertTrue(body.token.isNotBlank()) {
            "Token should not be empty or blank"
        }
    }

    private fun randomString(): String {
        val uuid = UUID.randomUUID().toString()
        return Base64.getEncoder().encode(uuid.toByteArray())
            .toString(Charsets.UTF_8)
            .substring(0, 20)
    }

    @Test
    fun `REGISTER user already exists`() = runTest {
        val response = client.register(
            RegisterRequest(
                email = "liza@mail.ru",
                password = "12345678",
                age = StubUser.AGE
            )
        )

        Assertions.assertEquals(HttpStatusCode.UnprocessableEntity, response.status)
    }
}