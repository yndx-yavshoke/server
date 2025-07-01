package io.github.lizalogvinenko.yavshoke.test.client.dto.login

import kotlinx.serialization.Serializable

@Serializable
data class LoginRequest(
    val email: String,
    val password: String
)