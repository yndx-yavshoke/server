package io.github.lizalogvinenko.yavshoke.test.client.dto.register

import kotlinx.serialization.Serializable

@Serializable
data class RegisterRequest(
    val email: String,
    val password: String,
    val age: Long
)