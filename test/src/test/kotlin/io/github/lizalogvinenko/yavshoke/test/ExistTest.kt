package io.github.lizalogvinenko.yavshoke.test

import io.github.lizalogvinenko.yavshoke.test.client.YavshokeClient
import io.github.lizalogvinenko.yavshoke.test.client.dto.exist.ExistRequest
import io.github.lizalogvinenko.yavshoke.test.client.dto.exist.ExistResponse
import io.ktor.client.call.body
import io.ktor.http.HttpStatusCode
import kotlinx.coroutines.test.runTest
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test

class ExistTest {
    val client = YavshokeClient.create()

    @Test
    fun `WHEN get existing user THEN exists`() = runTest {
        val response = client.exist(ExistRequest(email = "liza@example.com"))

        Assertions.assertEquals(HttpStatusCode.OK, response.status)
        Assertions.assertEquals(
            ExistResponse(exist = true),
            response.body<ExistResponse>()
        )
    }

    @Test
    fun `WHEN get not existing user THEN not exists`() = runTest {
        val response = client.exist(ExistRequest(email = "a.yakovlev@gmail.com"))

        Assertions.assertEquals(HttpStatusCode.OK, response.status)
        Assertions.assertEquals(
            ExistResponse(exist = false),
            response.body<ExistResponse>()
        )
    }
}