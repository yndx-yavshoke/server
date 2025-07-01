package io.github.lizalogvinenko.yavshoke.test

import io.github.lizalogvinenko.yavshoke.test.client.YavshokeClient
import io.github.lizalogvinenko.yavshoke.test.client.dto.login.LoginRequest
import io.github.lizalogvinenko.yavshoke.test.client.dto.login.LoginResponse
import io.github.lizalogvinenko.yavshoke.test.util.StubUser
import io.ktor.client.call.body
import io.ktor.http.HttpStatusCode
import kotlinx.coroutines.test.runTest
import org.junit.jupiter.api.Assertions
import kotlin.test.Test

class LoginTest {
    val client = YavshokeClient.create()

    @Test
    fun `LOGIN user`() = runTest {
        val response = client.login(
            LoginRequest(
                email = "liza@example.com",
                password = "12345678"
            )
        )

        Assertions.assertEquals(HttpStatusCode.OK, response.status)

        val body = response.body<LoginResponse>()

        Assertions.assertEquals(
            LoginResponse.User(
                id = body.user.id,
                email = "liza@example.com",
                name = body.user.name,
                age = StubUser.AGE
            ),
            body.user
        )

        Assertions.assertTrue(body.token.isNotBlank()) {
            "Token should not be empty or blank"
        }
    }

    @Test
    fun `LOGIN Validation error`() = runTest {
        val response = client.login(
            LoginRequest(
                email = "lizacapriza@mail.ru",
                password = "12345678910"
            )
        )

        Assertions.assertEquals(HttpStatusCode.UnprocessableEntity, response.status)
    }
}