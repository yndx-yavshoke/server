package io.github.lizalogvinenko.yavshoke.test

import io.github.lizalogvinenko.yavshoke.test.client.YavshokeClient
import io.github.lizalogvinenko.yavshoke.test.client.dto.user.GetUserResponse
import io.github.lizalogvinenko.yavshoke.test.util.StubUser
import io.github.lizalogvinenko.yavshoke.test.util.YavshokeSteps
import io.ktor.client.call.body
import io.ktor.http.HttpStatusCode
import kotlinx.coroutines.test.runTest
import org.junit.jupiter.api.Assertions
import kotlin.test.Test

class GetUserTest {
    private val client = YavshokeClient.create()
    private val steps = YavshokeSteps(client)

    @Test
    fun `GET user data`() = runTest {
        val authenticationResult = steps.createUserAndAuthenticate()

        val response = client.getUser(
            bearerToken = authenticationResult.token
        )

        Assertions.assertEquals(HttpStatusCode.OK, response.status)

        val body = response.body<GetUserResponse>()

        Assertions.assertEquals(
            GetUserResponse.User(
                id = body.user.id,
                email = authenticationResult.email,
                name = "Neko",
                age = StubUser.AGE
            ),
            body.user
        )
    }

    @Test
    fun `GET user data with not valid token`() = runTest {
        val response = client.getUser(
            bearerToken = "<not valid token>"
        )

        Assertions.assertEquals(HttpStatusCode.Unauthorized, response.status)
    }

    @Test
    fun `GET user data without token`() = runTest {
        val response = client.getUser(
            bearerToken = null
        )

        Assertions.assertEquals(HttpStatusCode.Unauthorized, response.status)
    }
}