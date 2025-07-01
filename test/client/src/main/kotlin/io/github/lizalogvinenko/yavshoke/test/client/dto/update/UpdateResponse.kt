package io.github.lizalogvinenko.yavshoke.test.client.dto.update

import kotlinx.serialization.Serializable

@Serializable
data class UpdateResponse(val user: User) {

    @Serializable
    data class User(
        val id: Long,
        val email: String,
        val name: String,
        val age: Long
    )
}