package fixtures

import data.User
import io.restassured.RestAssured
import io.restassured.http.ContentType
import io.restassured.response.Response

object UserHelper {

    fun register(user: User): String {
        return RestAssured
            .given()
            .contentType(ContentType.JSON)
            .body(mapOf(
                "email" to user.email,
                "name" to user.name,
                "age" to user.age,
                "password" to user.password
            ))
            .post("/auth/register")
            .then()
            .statusCode(200)
            .extract()
            .path("token")
    }

    fun login(user: User): String {
        return RestAssured
            .given()
            .contentType(ContentType.JSON)
            .body(mapOf(
                "email" to user.email,
                "password" to user.password
            ))
            .post("/auth/login")
            .then()
            .statusCode(200)
            .extract()
            .path("token")
    }

    fun updateName(token: String, newName: String): Response {
        return RestAssured
            .given()
            .contentType(ContentType.JSON)
            .header("Authorization", "Bearer $token")
            .body(mapOf("name" to newName))
            .patch("/user/name")
    }

    fun checkUserExists(email: String): Boolean {
        return RestAssured
            .given()
            .contentType(ContentType.JSON)
            .body(mapOf("email" to email))
            .post("/exist")
            .then()
            .statusCode(200)
            .extract()
            .path("exist")
    }
}