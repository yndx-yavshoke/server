package tests;

import io.restassured.response.Response;
import org.junit.jupiter.api.Test;
import Service.AuthService;
import resources.DataGenerator;

import static org.junit.jupiter.api.Assertions.*;
public class ShockTest {
    @Test
    public void userAlreadyRegistered(){
        String email = DataGenerator.generateUniqueEmail();
        String password = "okaydocky90";
        int age = DataGenerator.adultCat();

        //first regis!!
        AuthService.registerUser(email,password,age);
        //now we r checking if the email is exist !
        Response response = AuthService.checkUser(email);

        assertEquals(200, response.getStatusCode());
        assertTrue(response.jsonPath().getBoolean("exist"), "User in SHOK");
    }

    @Test
    public void userNotRegistered(){
        String email = DataGenerator.generateUniqueEmail();

        Response response = AuthService.checkUser(email);

        //The Server is Alive
        assertEquals(200, response.getStatusCode());

        //False means that NotExist!
        assertFalse(response.jsonPath().getBoolean("exist"), "User is NOT in SHOK");
    }

//    @Test
//    public void WithInvalidEmail() {
//        String email = "Hello_My_Name_Is_No_One";
//
//        Response response = AuthService.checkUser(email);

            //400 Bad Request or similar
//        assertEquals(200, response.getStatusCode(),
//                "invalid email");
//    }
//
//    @Test
//    public void rWithNullEmail() {
//        Response response = AuthService.checkUser(null);
//
//        //400 Bad Request or similar
//        assertEquals(200, response.getStatusCode(),
//        "null email input");
//    }
}
