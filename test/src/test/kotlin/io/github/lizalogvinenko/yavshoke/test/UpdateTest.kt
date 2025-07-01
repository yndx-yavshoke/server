package io.github.lizalogvinenko.yavshoke.test

import io.github.lizalogvinenko.yavshoke.test.client.YavshokeClient
import io.github.lizalogvinenko.yavshoke.test.client.dto.update.UpdateRequest
import io.github.lizalogvinenko.yavshoke.test.client.dto.update.UpdateResponse
import io.github.lizalogvinenko.yavshoke.test.util.StubUser
import io.github.lizalogvinenko.yavshoke.test.util.YavshokeSteps
import io.ktor.client.call.body
import io.ktor.http.HttpStatusCode
import kotlinx.coroutines.test.runTest
import org.junit.jupiter.api.Assertions
import kotlin.test.Test


class UpdateTest {
    private val client = YavshokeClient.create()
    private val steps = YavshokeSteps(client)

    @Test
    fun `UPDATE user`() = runTest {
        val authenticationResult = steps.createUserAndAuthenticate()

        val response = client.update(
            UpdateRequest(
                name = "Neko123"
            ),
            bearerToken = authenticationResult.token
        )

        Assertions.assertEquals(HttpStatusCode.OK, response.status)

        val body = response.body<UpdateResponse>()

        Assertions.assertEquals(
            UpdateResponse.User(
                id = body.user.id,
                email = authenticationResult.email,
                name = "Neko123",
                age = StubUser.AGE
            ),
            body.user
        )
    }

    @Test
    fun `UPDATE user with no token`() = runTest {
        val response = client.update(
            bearerToken = "",
            request = UpdateRequest(
                name = "Neko123"
            )
        )

        Assertions.assertEquals(HttpStatusCode.Unauthorized, response.status)
    }

    @Test
    fun `UPDATE user validation error`() = runTest {
        val response = client.update(
            bearerToken = "",
            request = UpdateRequest(
                name = ""
            )
        )

        Assertions.assertEquals(HttpStatusCode.UnprocessableEntity, response.status)
    }
}

