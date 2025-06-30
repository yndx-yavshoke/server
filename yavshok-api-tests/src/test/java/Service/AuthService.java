package Service;

import APIClient.AuthClient;
import io.restassured.response.Response;

public class AuthService {
    private static final  AuthClient authClient = new AuthClient();

    public static Response registerUser(String email, String password, int age){
        return authClient.register(email, password, age);
    }
    public static Response loginUser(String email, String password){
        return authClient.login(email, password);
    }
    public static Response checkUser(String email){
        return authClient.checkShock(email);
    }
    public static Response getUserProfile(String token){
        return authClient.getUserProfile(token);
    }
    public static Response updateUserName(String token, String newName){
        return authClient.changeUserName(token, newName);
    }
}
