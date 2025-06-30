package APIClient;

import io.restassured.response.Response;

import static io.restassured.RestAssured.given;

public class AuthClient extends BaseClient {
    public Response register(String email, String password, int age){
        String payload = String.format("{\"email\":\"%s\", \"password\":\"%s\", \"age\":%d}",
                email, password, age);

        return given()
                // .log().all()
                .header("Content-Type", "application/json")
                .body(payload)
                .when()
                .post("/auth/register");
    }

    public Response login(String email, String password){
        String payload = String.format("{\"email\":\"%s\", \"password\":\"%s\"}",
                email, password);

        return given()
                // .log().all()
                .header("Content-Type", "application/json")
                .body(payload)
                .when()
                .post("/auth/login");
    }

    public Response checkShock(String email){
        String payload = String.format("{\"email\":\"%s\"}", email);

        return given()
                //.log().all()
                .header("Content-Type", "application/json")
                .body(payload)
                .when()
                .post("/exist");
    }

    public Response getUserProfile(String token){
        return given()
                // .log().all()
                .header("Authorization", "Bearer " + token)
                .when()
                .get("/user/me");
    }
    public Response changeUserName(String token, String newName){
        String payload = String.format("{\"name\": \"%s\"}", newName);

        return given()
//                .log().all()
                .header("Authorization", "Bearer " + token)
                .header("Content-Type", "application/json")
                .body(payload)
                .when()
                .patch("/user/name");

    }
}
