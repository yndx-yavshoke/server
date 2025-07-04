package model

import kotlinx.serialization.Serializable


@Serializable
data class UserLogIn(
    val email: String,
    val password: String
)

@Serializable
data class UserName(
    val name: String
)

@Serializable
data class RegisterUser(
    val email: String,
    val password: String,
    val age: Int
)

@Serializable
data class ExistUserData(
    val email: String
)

@Serializable
data class Exist(
    val exist: Boolean
)

@Serializable
data class User(
    val id: Int,
    val email: String,
    val name: String,
    val age: Int
)

@Serializable
data class LoggedUser(
    val token: String,
    val user: User
)

@Serializable
data class UserMe(
    val user: User
)

@Serializable
data class ErrorMessage(
    val message: String
)

@Serializable
data class ErrorLogin(
    val fields: ErrorPassword
)

@Serializable
data class ErrorPassword(
    val password: String
)

