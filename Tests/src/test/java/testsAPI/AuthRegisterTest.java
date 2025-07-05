package testsAPI;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static utilsAPI.AuthHelper.*;

public class AuthRegisterTest extends BaseTest {

    @Test
    void successfulRegistration() {
        String email = generateRandomEmail();
        String password = generateRandomPass();
        int age = generateRandomAge();

        String body = String.format("{\"email\": \"%s\", \"password\": \"%s\", \"age\": %d}", email, password, age);

        Response response = RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/auth/register")
                .then()
                .statusCode(200)
                .extract().response();

        assertNotNull(response.path("token"));
        assertEquals(email, response.path("user.email"));
        assertEquals(age, (int) response.path("user.age"));
    }

    @Test
    void duplicateEmailRegistration() {
        String email = generateRandomEmail();
        String password = generateRandomPass();
        int age = generateRandomAge();

        String body = String.format("{\"email\": \"%s\", \"password\": \"%s\", \"age\": %d}", email, password, age);

        RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/auth/register")
                .then()
                .statusCode(200);

        RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/auth/register")
                .then()
                .statusCode(422);
    }

    @Test
    void missingEmailRegistration() {
        String password = generateRandomPass();
        int age = generateRandomAge();

        String body = String.format("{\"password\": \"%s\", \"age\": %d}", password, age);

        RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/auth/register")
                .then()
                .statusCode(422);
    }

    @Test
    void missingPasswordRegistration() {
        String email = generateRandomEmail();
        int age = generateRandomAge();

        String body = String.format("{\"email\": \"%s\", \"age\": %d}", email, age);

        RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/auth/register")
                .then()
                .statusCode(422);
    }

    @Test
    void invalidEmailFormatRegistration() {
        String email = "invalid.com";
        String password = generateRandomPass();
        int age = generateRandomAge();

        String body = String.format("{\"email\": \"%s\", \"password\": \"%s\", \"age\": %d}", email, password, age);

        RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/auth/register")
                .then()
                .statusCode(422);
    }
}

// Если бы пароль проверялся адекватно на бэкенде, то его бы тоже здесь побольше попроверял, но походу его ограничения в данном проекте обрабатываются лишь на фронтенде.