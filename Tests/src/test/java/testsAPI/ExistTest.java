package testsAPI;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.given;
import static org.junit.jupiter.api.Assertions.*;
import static utilsAPI.AuthHelper.*;

public class ExistTest extends BaseTest {

    @Test
    void existingUserCheck() {
        String email = generateRandomEmail();
        String password = generateRandomPass();
        int age = generateRandomAge();

        registerAndGetToken(email, password, age);

        String body = String.format("{\"email\": \"%s\"}", email);

        Response response = given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/exist");

        assertEquals(200, response.getStatusCode());
        assertTrue(response.jsonPath().getBoolean("exist"));
    }

    @Test
    void nonExistingUserCheck() {
        String email = generateRandomEmail() + "_no_such_user";
        String body = String.format("{\"email\": \"%s\"}", email);

        Response response = given()
                .contentType(ContentType.JSON)
                .body(body)
                .post("/exist");

        assertEquals(200, response.getStatusCode());
        assertFalse(response.jsonPath().getBoolean("exist"));
    }

    // Статус-коды для двух следующих тестов не указаны в JSON-схеме к проекту, но палятся при прогоне API на проде к этой "ручке" с пустым телом запроса или null'ом,
    // поэтому решил добавить эти тесты, потому что ошибки-то такие кейсы должны вернуть какие-то

    @Test
    void emptyBodyRequest() {
        Response response = given()
                .contentType(ContentType.JSON)
                .body("{}")
                .post("/exist");

        int status = response.getStatusCode();
        assertEquals(422, status);
    }

    @Test
    void nullBodyRequest() {
        Response response = given()
                .contentType(ContentType.JSON)
                .body("{null}")
                .post("/exist");

        int status = response.getStatusCode();
        assertEquals(400, status);
    }
}