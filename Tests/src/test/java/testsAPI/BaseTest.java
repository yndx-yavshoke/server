package testsAPI;

import io.restassured.RestAssured;
import org.junit.jupiter.api.BeforeAll;

public abstract class BaseTest {
    @BeforeAll
    static void setup() {
        RestAssured.baseURI = "http://localhost:3000";
    }
}