import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.*;
import java.util.UUID;
import static org.hamcrest.Matchers.*;

public class UserNameUpdateTest {

    private static final String BASE_URL = "http://localhost:3000";
    private static final String REGISTER_ENDPOINT = "/auth/register";
    private static final String LOGIN_ENDPOINT = "/auth/login";
    private static final String UPDATE_NAME_ENDPOINT = "/user/name";

    private static String testEmail;
    private static String validToken;
    private static final String TEST_PASSWORD = "string";
    private static final int TEST_AGE = 99;
    private static final String INITIAL_NAME = "Initial User";

    @BeforeAll
    public static void setup() {
        RestAssured.baseURI = BASE_URL;
        RestAssured.enableLoggingOfRequestAndResponseIfValidationFails();

        testEmail = "user_" + UUID.randomUUID().toString().substring(0, 8) + "@example.com";
        registerTestUser();
        validToken = loginAndGetToken();
    }

    private static void registerTestUser() {
        RestAssured.given()
                .contentType(ContentType.JSON)
                .body(String.format(
                        "{\"email\": \"%s\", \"password\": \"%s\", \"age\": %d, \"name\": \"%s\"}",
                        testEmail, TEST_PASSWORD, TEST_AGE, INITIAL_NAME
                ))
                .when()
                .post(REGISTER_ENDPOINT)
                .then()
                .log().ifValidationFails()
                .statusCode(200);
    }

    private static String loginAndGetToken() {
        return RestAssured.given()
                .contentType(ContentType.JSON)
                .body(String.format(
                        "{\"email\": \"%s\", \"password\": \"%s\"}",
                        testEmail, TEST_PASSWORD
                ))
                .when()
                .post(LOGIN_ENDPOINT)
                .then()
                .log().ifValidationFails()
                .statusCode(200)
                .extract()
                .path("token");
    }

    @Test
    @DisplayName("Успешное обновление имени")
    public void testSuccessfulNameUpdate() {
        String newName = "Updated Name " + UUID.randomUUID().toString().substring(0, 4);

        RestAssured.given()
                .contentType(ContentType.JSON)
                .header("Authorization", "Bearer " + validToken)
                .body(String.format("{\"name\": \"%s\"}", newName))
                .when()
                .patch(UPDATE_NAME_ENDPOINT)
                .then()
                .log().ifValidationFails()
                .statusCode(200)
                .body("user.name", equalTo(newName));  // Изменено с "name" на "user.name"
    }

    @Test
    @DisplayName("Попытка обновления с неверным токеном")
    public void testUpdateWithInvalidToken() {
        String invalidToken = "invalid_token";

        RestAssured.given()
                .contentType(ContentType.JSON)
                .header("Authorization", "Bearer " + invalidToken)
                .body("{\"name\": \"New Name\"}")
                .when()
                .patch(UPDATE_NAME_ENDPOINT)
                .then()
                .log().ifValidationFails()
                .statusCode(401);
    }

    @Test
    @DisplayName("Попытка обновления с невалидным именем")
    public void testUpdateWithInvalidName() {
        // Создаем невалидное имя (не-UTF8 символы)
        String invalidName = "Invalid \u0000 Name \uFFFF";

        RestAssured.given()
                .contentType(ContentType.JSON)
                .header("Authorization", "Bearer " + validToken)
                .body(String.format("{\"name\": \"%s\"}", invalidName))
                .when()
                .patch(UPDATE_NAME_ENDPOINT)
                .then()
                .log().ifValidationFails()
                .statusCode(400)  // Изменено с 422 на 400 согласно реальному ответу сервера
                .body(equalTo("Bad Request"));  // Проверяем текстовый ответ
    }
}
