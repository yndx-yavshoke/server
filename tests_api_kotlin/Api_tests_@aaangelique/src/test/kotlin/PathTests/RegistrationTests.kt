package ru.yavshok.tests.PathTests

import org.junit.jupiter.api.Test
import io.restassured.RestAssured
import org.junit.jupiter.api.Assertions.*
import ru.yavshok.tests.base.BaseApiTest
import ru.yavshok.tests.base.EmailGenerators.generateEmailWithLength
import ru.yavshok.tests.base.EmailGenerators.generateEmailNonLatin
import ru.yavshok.tests.base.EmailGenerators.generateEmailUpperCase
import ru.yavshok.tests.base.EmailGenerators.generateEmailWithSpecialChars
import ru.yavshok.tests.base.EmailGenerators.generateEmailWithDoubleDot





class UserRegistrationTests: BaseApiTest() {


    @Test
    fun `Successful Registration`() {
        val user = createRandomUser()
        val response = RestAssured.given(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
            .extract().response()

        assertEquals(200, response.statusCode)
    }

    @Test
    fun `Successful Registration with response body validation`() {
        val user = createRandomUser()

        val response = RestAssured.given(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
            .extract()
            .jsonPath()

        val token = response.getString("token")
        val responseEmail = response.getString("user.email")
        val userId = response.getInt("user.id")
        val age = response.getInt("user.age")

        // Проверки тела
        assertEquals(user.email, responseEmail)
        assertEquals(user.age, age)
        assertTrue(token.isNotBlank(), "Token should not be blank")
        assertTrue(userId > 0, "User ID should be positive")
    }


    @Test
    fun `Registration With Empty Fields returns 422`() {
        val user = emptyMap<String,Any>()

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()
            .statusCode(422)
    }

    @Test
    fun `Registration With Empty Email returns 422`(){
        val user = createRandomUser().copy(email = "")

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(422)
    }

    @Test
    fun `Registration With Empty Password returns 422`() {
        val user = createRandomUser().copy(password = "")

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(422)
    }

    @Test
    fun `Registration With Empty Age returns 422`() {
        val user = createRandomUser().copy(age = null)

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(422)
    }

    @Test
    fun `Registration With Empty Age and Pass returns 422`() {
        val user = createRandomUser().copy(password = "", age = null)

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(422)
    }

    @Test
    fun `Registration With Empty Email Pass returns 422`() {
        val user = createRandomUser().copy(email = "", password = "")

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(422)
    }

    @Test
    fun `Registration With Empty Email Age returns 422`() {
        val user = createRandomUser().copy(email = "", age = null)

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(422)
    }

    @Test
    fun `Email Without @ returns 422`(){
        val user = createRandomUser().copy(email = "userya.ru")

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(422)
    }

    @Test
    fun `Email Without domain returns 422`() {
        val user = createRandomUser().copy(email = "user@")

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(422)
    }

    @Test
    fun `Email Without Username returns 422`() {
        val user = createRandomUser().copy(email = "@ya.ru")

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(422)
    }

    @Test
    fun `Email With Spaces Inside returns 422`() {
        val user = createRandomUser().copy(email = "u ser @ya.ru")

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(422)

    }

    @Test
    fun `Trim Email With Surrounding Spaces`() {
        val user = createRandomUser().copy(email = " user@ya.ru ")

        RestAssured.given()
            .body(user)
            .`when`()
            .post("/auth/register")
            .then()

            .statusCode(200)
    }



    @Test
    fun `Register With Email longer than 51 char returns 422`() {
        val user = createRandomUser().copy(email = generateEmailWithLength(70))

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(422)
    }

    @Test
    fun `Register with email exactly 51 chars returns 422`() {
        val user = createRandomUser().copy(email = generateEmailWithLength(51))

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(422)
    }

    @Test
    fun `Register with email 50 chars returns 200`() {
        val user = createRandomUser().copy(email = generateEmailWithLength(50))

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
    }

    @Test
    fun `Register with email 49 chars returns 200`() {
        val user = createRandomUser().copy(email = generateEmailWithLength(49))

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
    }

    @Test
    fun `Register with email 48 chars returns 200`() {
        val user = createRandomUser().copy(email = generateEmailWithLength(48))

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
    }

    @Test
    fun `Register with email 6 chars returns 200`() {
        val user = createRandomUser().copy(email = generateEmailWithLength(6))

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
    }

    @Test
    fun `Register with email 5 chars returns 200`() {
        val user = createRandomUser().copy(email = generateEmailWithLength(5))

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
    }

    @Test
    fun `Register with email 4 chars returns 422`() {
        val user = createRandomUser().copy(email = generateEmailWithLength(4))

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
    }

    @Test
    fun `Register with valid special chars email succeeds`() {
        val email = generateEmailWithSpecialChars(true)
        val user = BaseApiTest.ExampleUser(email, "Password123", 30)

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
    }

    @Test
    fun `Register with invalid special chars email returns 422`() {
        val email = generateEmailWithSpecialChars(false)
        val user = BaseApiTest.ExampleUser(email, "Password123", 30)

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(422)
    }

    @Test
    fun `Register with double dot in username returns 422`() {
        val email = generateEmailWithDoubleDot()
        val user = BaseApiTest.ExampleUser(email, "Password123", 30)

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(422)
    }

    @Test
    fun `Register with uppercase email succeeds`() {
        val upperCaseEmail = generateEmailUpperCase()
        val user = createRandomUser().copy(email = upperCaseEmail)

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(200)
    }

    @Test
    fun `Register with non-latin email returns 422`() {
        val nonLatinEmail = generateEmailNonLatin()
        val user = createRandomUser().copy(email = nonLatinEmail)

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(422)
    }

    @Test
    fun `Register with already existing email returns 422`() {
        val user = createRandomUser()
        val registeredUser = registerUser(user)

        RestAssured.given()
            .spec(spec)
            .body(user)
            .post("/auth/register")
            .then()
            .statusCode(422)
    }
}