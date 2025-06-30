package APIClient;

import io.restassured.RestAssured;

public class BaseClient {
    static {
        RestAssured.baseURI = "http://localhost:3000";
    }
}
