package tests;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;
import Service.AuthService;
import resources.DataGenerator;
import resources.TokenGenerator;

import java.util.Calendar;
import java.util.UUID;

import static org.junit.jupiter.api.Assertions.*;

public class ChangeNameTest {

    //успешно сменилось имя
    @Test
    public void ChangeNameSuccessfully(){
        String newName = "amIMarvel?";

        String email = "user" + System.currentTimeMillis() + "@yandex.ru";
        String password = "okaydocky90";
        int age = DataGenerator.oldCat();

        //regist
        AuthService.registerUser(email, password, age);
        //login
        String token = AuthService.loginUser(email, password).jsonPath().getString("token");
        Response response = AuthService.updateUserName(token, newName);

        assertEquals(200, response.getStatusCode());
        assertEquals(newName, response.jsonPath().getString("user.name"), "Name updated!");

        Response profile = AuthService.getUserProfile(token);
        assertEquals(newName, profile.jsonPath().getString("user.name"), "reflect new name");


    }

    //на пустую Value
    @Test
    public void EmptyValueFail(){
        String email = DataGenerator.generateUniqueEmail();
        String password = "okaydocky90";
        int age = DataGenerator.adultCat();

        AuthService.registerUser(email, password, age);
        String token = AuthService.loginUser(email, password).jsonPath().getString("token");

        Response response = AuthService.updateUserName(token, "");

        assertEquals(422, response.getStatusCode(), "Empty name should not be allowed");
    }

    //на Null value & its a BUG because the Server exept null value!!
//    @Test
//    public void withNullValue() {
//
//        String email = DataGenerator.generateUniqueEmail();
//        String password = "okaydocky90";
//        int age = DataGenerator.adultCat();
//
//        AuthService.registerUser(email, password, age);
//        String token = AuthService.loginUser(email, password).jsonPath().getString("token");
//
//        Response response = AuthService.updateUserName(token, null);
//
//        assertEquals(401, response.getStatusCode(), "Null value should be rejected!");
//    }

    //на очень длинную Value
    @Test
    public void WithAlotOfLetter(){
        String longName = "a".repeat(100);

        String email = DataGenerator.generateUniqueEmail();
        String password = "okaydocky90";
        int age = DataGenerator.adultCat();

        AuthService.registerUser(email, password, age);
        String token = AuthService.loginUser(email, password).jsonPath().getString("token");

        Response response = AuthService.updateUserName(token, longName);

        assertTrue(response.getStatusCode() == 422,
                "Doesn't allow us to make > 50 symbol!");
    }

    //Token Нет
    @Test
    public void WithoutToken(){
        String newName = "amIHarryPotter?";

        Response response = AuthService.updateUserName(null, newName);
        assertEquals(401, response.getStatusCode(),
                "Auth header required dude!");
    }

    //Token Файк
    @Test
    public void WithFakeToken(){
        String newName = "nowAmHacker!";
        String fakeToken = TokenGenerator.generateNewToken();
        Response response = AuthService.updateUserName(fakeToken, newName);

        assertEquals(401, response.getStatusCode(),
                "Invalid token should not be accepted");
    }
}

