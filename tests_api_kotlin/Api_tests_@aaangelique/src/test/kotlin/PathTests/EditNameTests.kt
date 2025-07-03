package ru.yavshok.tests.PathTests

import io.restassured.RestAssured
import org.hamcrest.Matchers.*
import org.junit.jupiter.api.Test
import ru.yavshok.tests.base.BaseApiTest
import org.junit.jupiter.api.BeforeAll

class UpdateUserNameTests : BaseApiTest() {
    private lateinit var authToken: String
    @BeforeAll
    fun setup() {
        val user = createRandomUser()
        registerUser(user)
        authToken = loginAndGetToken(user.email, user.password)
    }
    @Test
    fun `Update user name successfully returns 200`() {
        val user = createRandomUser()
        registerUser(user)
        val token = loginAndGetToken(user.email,user.password)
        val newName = "YourNewName"

        RestAssured.given()
            .spec(spec)
            .header("Authorization", "Bearer ${authToken}")
            .body(mapOf("name" to newName))
            .patch("/user/name")
            .then()
            .statusCode(200)
            .body("user.name", equalTo(newName))
            .body("user.email", notNullValue())
            .body("user.id", greaterThan(0))
    }

    @Test
    fun `Update user name without token returns 401`() {
        RestAssured.given()
            .spec(spec)
            .body(mapOf("name" to "AnyName"))
            .patch("/user/name")
            .then()
            .statusCode(401)
            .body("message", not(emptyString()))
    }

    @Test
    fun `Update user name with empty name returns 422`() {
        RestAssured.given()
            .spec(spec)
            .header("Authorization", "Bearer ${authToken}")
            .body(mapOf("name" to ""))
            .patch("/user/name")
            .then()
            .statusCode(422)
    }
}