import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;

import static io.restassured.RestAssured.given;

public class APIClient {
    private final RequestSpecification spec;

    public APIClient(RequestSpecification spec) {
        this.spec = spec;
    }

    public Response register(User user) {
        Response response = given()
                .spec(spec)
                .body(user)
                .when()
                .post("/auth/register");
        user.setName(response.jsonPath().getString("user.name"));
        user.setToken(response.jsonPath().getString("token"));
        return response;
    }

    public Response exist(User user) {
        return given()
                .spec(spec)
                .body(user)
                .when()
                .post("/exist");
    }

    public Response login(User user) {
        return given()
                .spec(spec)
                .body(user)
                .when()
                .post("/auth/login");
    }

    public Response me(User user) {
        return given()
                .spec(spec)
                .header("Authorization", "Bearer " + user.getToken())
                .when()
                .get("user/me");
    }

    public Response changeName(User user, String newName) {
        String json = String.format("{\"name\": \"%s\"}", newName);
        Response response= given()
                .spec(spec)
                .header("Authorization", "Bearer " + user.getToken())
                .body(json)
                .when()
                .patch("user/name");
        user.setName(response.jsonPath().getString("user.name"));
        return response;
    }
}
