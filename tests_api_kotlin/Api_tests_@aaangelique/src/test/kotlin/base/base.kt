package ru.yavshok.tests.base


import io.restassured.RestAssured
import io.restassured.http.ContentType
import io.restassured.specification.RequestSpecification
import org.junit.jupiter.api.BeforeAll
import org.junit.jupiter.api.TestInstance
import kotlin.random.Random

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
open class BaseApiTest {

    protected lateinit var spec: RequestSpecification

    //создание клиента
    @BeforeAll
    fun globalSetup() {
        RestAssured.baseURI = "http://localhost:3000"
        spec = RestAssured
            .given()
            .contentType(ContentType.JSON)
            .accept(ContentType.JSON)
            .log().all()
    }

    data class ExampleUser(
        val email: String,
        val password: String,
        val age: Int?
    )

    // создание рандомного пользователя
    fun createRandomUser(): ExampleUser {
        val randomId = Random.nextInt(1000, 9999)
        return ExampleUser(
            email = "testuser$randomId@example.com",
            password = "Pass${Random.nextInt(100, 999)}",
            age = Random.nextInt(0, 99)
        )
    }

    // регистрация пользователя
    fun registerUser(user: ExampleUser = createRandomUser()): ExampleUser {
       val response = RestAssured
           .given()
           .spec(spec)
           .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
           .extract()
           .response()
        println("Register response: ${response.body.asString()}")
        return user
    }

    //получение токена авторизации
    fun loginAndGetToken(email: String, password: String): String {
        val response = RestAssured.given()
            .spec(spec)
            .body(mapOf("email" to email, "password" to password))
            .post("/auth/login")
            .then()
            .statusCode(200)
            .extract()
            .response()
        return response.jsonPath().getString("token") //
    }
}
