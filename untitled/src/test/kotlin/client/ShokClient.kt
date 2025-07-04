package client

import io.restassured.RestAssured
import io.restassured.response.Response
import io.restassured.http.ContentType
import model.ErrorLogin
import model.ErrorMessage
import model.Exist
import model.ExistUserData
import model.LoggedUser
import model.RegisterUser
import model.UserLogIn
import model.UserMe
import model.UserName
import org.apache.http.HttpStatus
import utils.JsonUtils


open class ShokClient {

    private val baseUrl = "http://localhost:3000"  // "https://api.yavshok.ru"


    fun existUser(existUserData: ExistUserData) : Exist{
        val response: Response = RestAssured.given()
            .contentType(ContentType.JSON)
            .body(JsonUtils.toJson(existUserData))
            .post("${baseUrl}/exist")

        return JsonUtils.fromJson<Exist>(response.body.asString())
    }

    fun loginUser(userLogIn: UserLogIn) : LoggedUser{
        val response: Response = RestAssured.given()
            .contentType(ContentType.JSON)
            .body(JsonUtils.toJson(userLogIn))
            .post("${baseUrl}/auth/login")
            .then()
            .extract()
            .response()

        return JsonUtils.fromJson<LoggedUser>(response.body.asString())
    }

    fun renameUser(name: UserName, token: String) : UserMe {
        val response: Response = RestAssured.given()
            .contentType(ContentType.JSON)
            .auth().oauth2(token)
            .body(JsonUtils.toJson(name))
            .patch("${baseUrl}/user/name")
        return JsonUtils.fromJson<UserMe>(response.body.asString())
    }

    fun registerUser(registerUser: RegisterUser) : LoggedUser {
        val response: Response = RestAssured.given()
            .contentType(ContentType.JSON)
            .body(JsonUtils.toJson(registerUser))
            .post("${baseUrl}/auth/register")
        return JsonUtils.fromJson<LoggedUser>(response.body.asString())
    }

    fun userMe(token: String) : UserMe {
        val response: Response = RestAssured.given()
            .auth().oauth2(token)
            .get("${baseUrl}/user/me")
        return JsonUtils.fromJson<UserMe>(response.body.asString())
    }

    fun userMeInvalid(token: String) : Pair<Int, ErrorMessage> {
        val response: Response = RestAssured.given()
            .auth().oauth2(token)
            .get("${baseUrl}/user/me")
            .then()
            .extract()
            .response()

        return Pair(response.statusCode, JsonUtils.fromJson<ErrorMessage>(response.body.asString()))
    }

    fun errorLoginUser(userLogIn: UserLogIn) : Pair<Int, ErrorLogin> {
        val response: Response = RestAssured.given()
            .contentType(ContentType.JSON)
            .body(JsonUtils.toJson(userLogIn))
            .post("${baseUrl}/auth/login")
            .then()
            .extract()
            .response()

        return Pair(response.statusCode, JsonUtils.fromJson<ErrorLogin>(response.body.asString()))
    }



}