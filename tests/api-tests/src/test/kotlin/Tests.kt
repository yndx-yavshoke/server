import data.User
import fixtures.UserHelper
import io.restassured.RestAssured
import org.junit.jupiter.api.BeforeAll
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.Assertions.*
import java.util.*

class UserFlowTest {

    companion object {
        private lateinit var user: User
        private lateinit var token: String

        @JvmStatic
        @BeforeAll
        fun setup() {
            RestAssured.baseURI = "http://localhost"
            RestAssured.port = 3000

            user = User(
                email = "user_${UUID.randomUUID()}@test.com",
                name = "Test User",
                age = 25,
                password = "secret123"
            )
            token = UserHelper.register(user)
            
        }
    }

    @Test
    fun `can get current user data`() {
        val response = RestAssured
            .given()
            .header("Authorization", "Bearer $token")
            .get("/user/me")
            .then()
            .statusCode(200)
            .extract()

        val returnedName = response.path<String>("user.name")
        assertEquals("Neko", returnedName)
    }

    @Test
    fun `can update user name`() {
        val newName = "Updated Name"
        token = UserHelper.login(user) 

        val response = UserHelper.updateName(token, newName)
        val actualName = response.then().statusCode(200).extract().path<String>("user.name")
        assertEquals(newName, actualName)
    }

    @Test
    fun `check if user exists returns true`() {
        assertTrue(UserHelper.checkUserExists(user.email))
    }

    @Test
    fun `check if user exists returns false`() {
        val email = "user_${UUID.randomUUID()}@test.com"
        assertFalse(UserHelper.checkUserExists(email))
    }
}
