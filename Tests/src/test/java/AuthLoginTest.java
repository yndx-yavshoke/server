import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.*;
import java.util.UUID;
import static org.hamcrest.Matchers.*;

public class AuthLoginTest {

    private static final String BASE_URL = "http://localhost:3000";
    private static final String REGISTER_ENDPOINT = "/auth/register";
    private static final String LOGIN_ENDPOINT = "/auth/login";

    private static String testEmail;
    private static final String TEST_PASSWORD = "string";
    private static final int TEST_AGE = 99;

    @BeforeAll
    public static void setup() {
        RestAssured.baseURI = BASE_URL;
        RestAssured.enableLoggingOfRequestAndResponseIfValidationFails();

        testEmail = "user_" + UUID.randomUUID().toString().substring(0, 8) + "@example.com";
        registerTestUser();
    }

    private static void registerTestUser() {
        RestAssured.given()
                .contentType(ContentType.JSON)
                .body(String.format(
                        "{\"email\": \"%s\", \"password\": \"%s\", \"age\": %d}",
                        testEmail, TEST_PASSWORD, TEST_AGE
                ))
                .when()
                .post(REGISTER_ENDPOINT)
                .then()
                .log().ifValidationFails()
                .statusCode(200);
    }

    @Test
    @DisplayName("Успешная авторизация с валидными данными")
    public void testSuccessfulLogin() {
        RestAssured.given()
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
                .body("token", notNullValue())
                .body("user.email", equalTo(testEmail))
                .body("user.age", equalTo(TEST_AGE));
    }

    @Test
    @DisplayName("Неудачная авторизация с неверным паролем")
    public void testFailedLoginWithWrongPassword() {
        RestAssured.given()
                .contentType(ContentType.JSON)
                .body(String.format(
                        "{\"email\": \"%s\", \"password\": \"wrong_password\"}",
                        testEmail
                ))
                .when()
                .post(LOGIN_ENDPOINT)
                .then()
                .log().ifValidationFails()
                .statusCode(422)
                .body("fields.password", equalTo("Неправильный логин или пароль"));
    }
}