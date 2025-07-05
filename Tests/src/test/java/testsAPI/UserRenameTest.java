package testsAPI;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.UUID;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static utilsAPI.AuthHelper.*;

public class UserRenameTest extends BaseTest {

    private String token;

    String newName = "NekoArcueid" + UUID.randomUUID().toString().substring(0, 5);

    @BeforeEach
    void initUser() {
        String email = generateRandomEmail();
        String password = generateRandomPass();
        int age = generateRandomAge();

        token = registerAndGetToken(email, password, age);

    }

    @Test
    void successfulNameUpdate() {
        Response response = RestAssured
                .given()
                .header("Authorization", "Bearer " + token)
                .contentType(ContentType.JSON)
                .body(String.format("{\"name\": \"%s\"}", newName))
                .when()
                .patch("/user/name")
                .then()
                .statusCode(200)
                .extract().response();

        String returnedName = response.path("user.name");
        assertEquals(newName, returnedName);
    }

    @Test
    void missingTokenNameUpdate() {
        RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(String.format("{\"name\": \"%s\"}", newName))
                .patch("/user/name")
                .then()
                .statusCode(401);
    }

    @Test
    void emptyNameUpdate() {
        RestAssured
                .given()
                .header("Authorization", "Bearer " + token)
                .contentType(ContentType.JSON)
                .body("{\"name\": \"\"}")
                .patch("/user/name")
                .then()
                .statusCode(422);
    }

    @Test
    void maxLengthNameUpdate() {
        String longName = "L".repeat(50);

        RestAssured
                .given()
                .header("Authorization", "Bearer " + token)
                .contentType(ContentType.JSON)
                .body(String.format("{\"name\": \"%s\"}", longName))
                .patch("/user/name")
                .then()
                .statusCode(200);
    }

    @Test
    void overMaxLengthNameUpdate() {
        String longName = "L".repeat(51);

        RestAssured
                .given()
                .header("Authorization", "Bearer " + token)
                .contentType(ContentType.JSON)
                .body(String.format("{\"name\": \"%s\"}", longName))
                .patch("/user/name")
                .then()
                .statusCode(422);
    }
}