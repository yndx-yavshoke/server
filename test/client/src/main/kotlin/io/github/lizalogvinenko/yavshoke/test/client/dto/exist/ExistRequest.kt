package io.github.lizalogvinenko.yavshoke.test.client.dto.exist

import kotlinx.serialization.Serializable

@Serializable
data class ExistRequest(val email: String)