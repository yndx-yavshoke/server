package tests;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;
import Service.AuthService;
import resources.DataGenerator;

import static org.junit.jupiter.api.Assertions.*;

public class LoginTests {

    @Test()
    public void normalLoginWithToken(){
        String email = DataGenerator.generateUniqueEmail();
        String password = "okaydocky90";

        //we should make regist first
        AuthService.registerUser(email, password, 26);
        //now login
        Response response = AuthService.loginUser(email, password);

        assertEquals(200, response.getStatusCode(), "200 We Are In!");
        assertTrue(response.jsonPath().getString("token").length() > 10, "Token Back");
    }

    @Test
    public void WithEmptyValues(){
        Response response = AuthService.loginUser("", "");

        assertEquals(422, response.getStatusCode(),
                "empty email and password!!");
    }

    @Test
    public void WithNullValues(){
        Response response = AuthService.loginUser(null, "okaydocky90");
        assertEquals(422, response.getStatusCode(), "The Email is Null!!");

        response = AuthService.loginUser(DataGenerator.generateUniqueEmail(), null);
        assertEquals(422, response.getStatusCode(),
                "The pass is Null!!");
    }

    @Test
    public void WithSQLInjection(){
        String email = "' OR '1'='1";
        String password = "' OR '1'='1";

        Response response = AuthService.loginUser(email, password);

        assertEquals(422, response.getStatusCode(),
                "no SQL injection, We Are Save 🔫 ");
    }

    @Test
    public void WithInvalidPassword(){
        String email = DataGenerator.generateUniqueEmail();
        String password = "okaydocky90";

        //also we should make regist first
        AuthService.registerUser(email, password, 26);
        //now login)
        Response response = AuthService.loginUser(email, "12345678m");

        assertEquals(422, response.getStatusCode(),
                "Неправильный логин или пароль");
    }

    @Test
    public  void loginWithInvalidEmailFormat(){
        Response response = AuthService.loginUser("shokbok23yandex.ru", "okaydocky90");

        assertEquals(422, response.getStatusCode(),
                "email validation error");
    }
}
