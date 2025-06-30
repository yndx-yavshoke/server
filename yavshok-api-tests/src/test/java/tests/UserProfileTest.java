package tests;

import io.restassured.response.Response;
import org.junit.jupiter.api.Test;
import Service.AuthService;
import resources.DataGenerator;

import static org.junit.jupiter.api.Assertions.*;
public class UserProfileTest {

    @Test
    public void WithInvalidToken() {
        String fakeToken = "3857892359825#$#@$@#$#@$%235hfibdifbd";

        Response response = AuthService.getUserProfile(fakeToken);

        assertEquals(401, response.getStatusCode(),
                "Fake TOKEN!!");
    }

    @Test
    public void WithNullToken() {
        Response response = AuthService.getUserProfile(null);

        assertEquals(401, response.getStatusCode(),
                "there is no token!!");
    }
}
