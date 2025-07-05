package testsAPI;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static utilsAPI.AuthHelper.*;

public class AuthLoginTest extends BaseTest {

    @Test
    void loginSuccess() {
        String email = generateRandomEmail();
        String password = generateRandomPass();
        int age = generateRandomAge();

        registerAndGetToken(email, password, age);

        String body = String.format("{\"email\": \"%s\", \"password\": \"%s\"}", email, password);

        Response response = RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/auth/login")
                .then()
                .statusCode(200)
                .extract().response();

        assertNotNull(response.path("token"));
        assertNotNull(response.path("user.id"));
    }

    @Test
    void loginFullyInvalidCredentials() {
        String email = "invalid.com";
        String password = "thisisverywrongpass123";

        String body = String.format("{\"email\": \"%s\", \"password\": \"%s\"}", email, password);

        RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/auth/login")
                .then()
                .statusCode(422);
    }

    @Test
    void loginMissingEmail() {
        String email = generateRandomEmail();
        String password = generateRandomPass();
        int age = generateRandomAge();

        registerAndGetToken(email, password, age);

        String body = String.format("{\"password\": \"%s\"}", password);

        RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/auth/login")
                .then()
                .statusCode(422);
    }

    @Test
    void loginMissingPassword() {
        String email = generateRandomEmail();
        String password = generateRandomPass();
        int age = generateRandomAge();

        registerAndGetToken(email, password, age);

        String body = String.format("{\"email\": \"%s\"}", email);

        RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/auth/login")
                .then()
                .statusCode(422);
    }
}