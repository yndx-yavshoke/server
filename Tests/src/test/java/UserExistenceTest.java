import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import java.util.UUID;
import static org.hamcrest.Matchers.*;

public class UserExistenceTest {

    @BeforeAll
    public static void setup() {
        RestAssured.baseURI = "http://localhost:3000";
        RestAssured.enableLoggingOfRequestAndResponseIfValidationFails();
    }

    @Test
    public void testUserExistence() {
        // Генерируем уникальный email при каждом запуске теста
        String email = "user_" + System.currentTimeMillis() % 100000 + "@gmail.com";
        String password = "VerySecurePass123!";
        int age = 30;
        String username = "user_" + UUID.randomUUID().toString().substring(0, 8);

        // Проверка, что пользователя нет
        RestAssured.given()
                .contentType(ContentType.JSON)
                .body(String.format("{\"email\": \"%s\"}", email))
                .when()
                .post("/exist")
                .then()
                .statusCode(200)
                .body("exist", equalTo(false));

        // Регистрация
        RestAssured.given()
                .contentType(ContentType.JSON)
                .body(String.format(
                        "{\"email\": \"%s\", \"password\": \"%s\", \"age\": %d, \"username\": \"%s\"}",
                        email, password, age, username
                ))
                .when()
                .post("/auth/register")
                .then()
                .log().all()  // Логируем ответ для диагностики
                .statusCode(200)
                .body("token", notNullValue())
                .body("user.email", equalTo(email));

        // Проверка, что пользователь теперь существует
        RestAssured.given()
                .contentType(ContentType.JSON)
                .body(String.format("{\"email\": \"%s\"}", email))
                .when()
                .post("/exist")
                .then()
                .statusCode(200)
                .body("exist", equalTo(true));
    }
}