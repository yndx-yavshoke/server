import io.restassured.builder.RequestSpecBuilder;
import io.restassured.filter.log.LogDetail;
import io.restassured.http.ContentType;
import io.restassured.specification.RequestSpecification;
import io.restassured.response.Response;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.hamcrest.Matchers.*;

public class APITests {
    private final RequestSpecification requestSpec = new RequestSpecBuilder()
            .setBaseUri("http://localhost:3000")
            .setAccept(ContentType.JSON)
            .setContentType(ContentType.JSON)
            .log(LogDetail.ALL)
            .build();
    private final DataHelper dataHelper = new DataHelper();
    private final APIClient apiClient = new APIClient(requestSpec);

    @Test
    void shouldRegisterNewUser() {
        User user = dataHelper.generateUser();
        Response response = apiClient.register(user);
        response.then()
                .statusCode(200)
                .body("token", notNullValue())
                .body("token", not(equalTo("0")))
                .body("token", not(isEmptyOrNullString()));
    }

    @Test
    void shouldNotRegisterExistingUser() {
        User user = dataHelper.generateUser();
        apiClient.register(user);

        Response response = apiClient.register(user);
        response.then().statusCode(422);
    }

    @Test
    void registeredUserShouldPassSHOKCheck() {
        User user = dataHelper.generateUser();
        apiClient.register(user);

        Response response = apiClient.exist(user);
        response.then()
                .statusCode(200)
                .body("exist", equalTo(true));
    }

    @Test
    void unregisteredUserShouldNoPassSHOKCheck() {
        User user = dataHelper.generateUser();

        Response response = apiClient.exist(user);
        response.then()
                .statusCode(200)
                .body("exist", equalTo(false));
    }

    @Test
    void shouldLoginWithRegisteredUser() {
        User user = dataHelper.generateUser();
        apiClient.register(user);

        Response response = apiClient.login(user);
        response.then()
                .statusCode(200)
                .body("token", notNullValue())
                .body("token", not(equalTo("0")))
                .body("token", not(isEmptyOrNullString()));
    }

    @Test
    void shouldNotLoginWithUnregisteredUser() {
        User user = dataHelper.generateUser();

        Response response = apiClient.login(user);
        response.then().statusCode(422);
    }

    @Test
    void shouldChangeNameRegisterUser() {
        User user = dataHelper.generateUser();
        apiClient.register(user);

        String expectedNewName = dataHelper.name();
        Response responseChangeName = apiClient.changeName(user, expectedNewName);
        responseChangeName.then().statusCode(200);

        String actualNewName = apiClient.me(user).jsonPath().getString("user.name");

        Assertions.assertEquals(expectedNewName, actualNewName);
    }
}
