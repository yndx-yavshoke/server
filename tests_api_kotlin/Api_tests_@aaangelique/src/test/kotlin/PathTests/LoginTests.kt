package ru.yavshok.tests.PathTests

import io.restassured.RestAssured
import org.hamcrest.Matchers
import ru.yavshok.tests.base.BaseApiTest
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertTrue
import kotlin.random.Random


class LogInTests: BaseApiTest()  {

    @Test
    fun `Successful login after registration`() {
        val user = registerUser()
        val loginRequest = mapOf(
            "email" to user.email,
            "password" to user.password
        )
        val response = spec.body(loginRequest)
            .post("/auth/login")
            .then()
            .statusCode(200)
            .extract()
            .jsonPath()
        val token = response.getString("token")
        val email = response.getString("user.email")

        assertEquals(user.email, email)
        assertTrue(token.isNotBlank())
    }

    @Test
    fun `Login with unregistered user returns 422`() {
        val fakeUser = ExampleUser(
            email = "notexists${Random.nextInt(10000, 99999)}@example.com",
            password = "Password123",
            age = Random.nextInt(0,99)
        )

        val response = RestAssured.given()
            .spec(spec)
            .body(mapOf("email" to fakeUser.email, "password" to fakeUser.password))
            .post("/auth/login")
            .then()
            .statusCode(422)
            .extract()
            .response()
        assert(response.jsonPath().getMap<String, Any>("fields").isNotEmpty())
        }

    @Test
    fun `Login with empty email and password returns 422`() {
        RestAssured.given()
            .spec(spec)
            .body(mapOf("email" to "", "password" to ""))
            .post("/auth/login")
            .then()
            .statusCode(422)
    }

    @Test
    fun `Login with empty email returns 422`() {
        val user = createRandomUser()

        RestAssured.given()
            .spec(spec)
            .body(mapOf("email" to "", "password" to user.password))
            .post("/auth/login")
            .then()
            .statusCode(422)
    }

    @Test
    fun `Login with empty password returns 422`() {
        val user = createRandomUser()

        RestAssured.given()
            .spec(spec)
            .body(mapOf("email" to user.email, "password" to ""))
            .post("/auth/login")
            .then()
            .statusCode(422)
    }

    @Test
    fun `Login with wrong password returns 422`() {
        val user = registerUser()

        RestAssured.given()
            .spec(spec)
            .body(mapOf("email" to user.email, "password" to "WrongPassword123"))
            .post("/auth/login")
            .then()
            .statusCode(422)
            .body("fields.password", Matchers.notNullValue())
    }

    @Test
    fun `Login with unregistered email but registered password returns 422`() {
        val user = registerUser()

        val fakeEmail = "unregistered${Random.nextInt(1000, 9999)}@example.com"

        RestAssured.given()
            .spec(spec)
            .body(mapOf("email" to fakeEmail, "password" to user.password))
            .post("/auth/login")
            .then()
            .statusCode(422)
    }





}

