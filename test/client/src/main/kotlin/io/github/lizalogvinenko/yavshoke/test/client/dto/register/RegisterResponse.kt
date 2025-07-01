package io.github.lizalogvinenko.yavshoke.test.client.dto.register

import kotlinx.serialization.Serializable

@Serializable
data class RegisterResponse(val token: String, val user: User) {

    @Serializable
    data class User(
        val id: Long,
        val email: String,
        val name: String,
        val age: Long
    )
}