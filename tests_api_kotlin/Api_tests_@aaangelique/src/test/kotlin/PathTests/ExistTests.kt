package ru.yavshok.tests.PathTests

import io.restassured.RestAssured
import org.hamcrest.Matchers.equalTo
import org.junit.jupiter.api.Test
import ru.yavshok.tests.base.BaseApiTest

class ExistTests : BaseApiTest() {

    @Test
    fun `Existing user returns exist true`() {
        val user = registerUser()

        RestAssured.given()
            .spec(spec)
            .body(mapOf("email" to user.email))
            .post("/exist")
            .then()
            .statusCode(200)
            .body("exist", equalTo(true))
    }

    @Test
    fun `Non-existing user returns exist false`() {
        val nonExistingEmail = "nonexistent_${System.currentTimeMillis()}@example.com"

        RestAssured.given()
            .spec(spec)
            .body(mapOf("email" to nonExistingEmail))
            .post("/exist")
            .then()
            .statusCode(200)
            .body("exist", equalTo(false))
    }

//    @Test
//    fun `Missing email field returns 400 or 422`() {
//        RestAssured.given()
//            .spec(spec)
//            .body("{}")
//            .post("/exist")
//            .then()
//            .statusCode(422) // в свагере пока нет кода ошибки. на будущее
//    }

//    @Test
//    fun `Empty email string returns 400 or 422`() {
//        RestAssured.given()
//            .spec(spec)
//            .body(mapOf("email" to ""))
//            .post("/exist")
//            .then()
//            .statusCode(422) - тоже на будущее
//    }

//    @Test
//    fun `Invalid email format returns error`() {
//        RestAssured.given()
//            .spec(spec)
//            .body(mapOf("email" to "not-an-email"))
//            .post("/exist")
//            .then()
//            .statusCode(422) на будущее
//    }
}