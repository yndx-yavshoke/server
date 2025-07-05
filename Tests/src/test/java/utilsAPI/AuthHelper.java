package utilsAPI;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;

import java.util.*;

public class AuthHelper {

    public static String generateRandomEmail() {
        return "test_" + UUID.randomUUID().toString().substring(0, 6) + "@yandex.ru";
    }

    public static String generateRandomPass() {
        return "Pass_" + UUID.randomUUID().toString().substring(0, 10);
    }

    // !!! У нас бэкенд не проверяет возраст почти что никак (и даже спокойно принимает и добавляет в БД его отрицательное значение и значения возраста больше 99),
    // поэтому в рамках данного пула ПОКА не буду делить юзеров на три "статусных" возрастных группы и проверять граничные значения (оставлю для галочки диапазон [0;99]),
    // ибо походу это по неописанной задумке ШОКа проверяется на фронтенде - тут чёрт его поймёшь, на каком по требованиям программном уровне этот возраст надо проверять.
    public static int generateRandomAge() {
        Random rndNumber = new Random();
        return rndNumber.nextInt(0,99);
    }

    public static String registerAndGetToken(String email, String password, int age) {
        String body = String.format("{\"email\": \"%s\", \"password\": \"%s\", \"age\": %d}", email, password, age);

        Response response = RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(body)
                .when()
                .post("/auth/register")
                .then()
                .statusCode(200)
                .extract().response();

        return response.path("token");
    }
}