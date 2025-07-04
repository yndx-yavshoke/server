package tests

import model.ExistUserData
import model.RegisterUser
import model.UserLogIn
import model.UserName
import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.api.MethodOrderer
import org.junit.jupiter.api.Order
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.TestMethodOrder
import org.junit.jupiter.api.assertAll
import utils.baseTest
import utils.randomAge
import utils.randomEmail
import utils.randomErrorPassword
import utils.randomName
import utils.randomPassword
import kotlin.test.assertEquals


@TestMethodOrder(MethodOrderer.OrderAnnotation::class)
class ShokApiTests: baseTest() {

    companion object{
        private val emailYang = randomEmail()
        private val emailAdult = randomEmail()
        private val emailOld = randomEmail()
        private val passwordYang = randomPassword()
        private val passwordAdult = randomPassword()
        private val passwordOld = randomPassword()
        private val ageYang = randomAge("yang")
        private val ageAdult = randomAge("adult")
        private val ageOld = randomAge("old")
        lateinit var newYangToken: String
        lateinit var newAdultToken: String
        lateinit var newOldToken: String

    }

    @Test
    @Order(1)
    fun registerNewUserYang(){
        println("\n[1 - Тест] Регистрация новго пользователя. (Молоденький котик)")

        val newUser = shokClient.registerUser(RegisterUser(
            emailYang,
            passwordYang,
            age = ageYang))

        assertAll(
            {println("Закинули данные с новым пользователем.")},
            {assertThat(newUser.user.email).isEqualTo(emailYang)},
            {println("Проверка произведена пользователь зарегистрирован: ${newUser}")}
        )
    }

    @Test
    @Order(2)
    fun existEmailYangTestTrue(){
        println("\n[2 - Тест] Проерка наличия emailYang. (Зарегистрированный)")

        val existEmail = shokClient.existUser(ExistUserData(emailYang))

        assertAll(
            {println("Email введен, ответ от сервера получен, сверяем.")},
            {assertThat(existEmail.exist).isEqualTo(true)}
        )
        println("Тест выполнен: результат проверки (шоковсти)- ${existEmail.exist}")
    }

    @Test
    @Order(3)
    fun loginYangUserTrue(){
        println("\n[3 - Тест] Вход зарегистрированного молодого пользователя.")

        val loginUser = shokClient.loginUser(UserLogIn(emailYang, passwordYang))

        assertAll(
            {println("Проверка входа пользователя")},
            {assertThat(loginUser.user.email).isEqualTo(emailYang)}
        )
        println("Тест выполнен: результат - ${loginUser.user.email}")
        println(loginUser)
        newYangToken = loginUser.token
    }

    @Test
    @Order(4)
    fun newNameYangUser(){
        println("\n[4 - Тест] Изменение имени молодого пользователя")
        val name = randomName()
        val renameUser = shokClient.renameUser(UserName(name), newYangToken)
        assertAll(
            {println("Проверка входа пользователя")},
            {assertThat(renameUser.user.name).isEqualTo(name)}
        )
        println("Тест выполнен: результат - ${renameUser.user.name}")
        println(renameUser)

    }

    @Test
    @Order(5)
    fun registerNewUserAdult(){
        println("\n[5 - Тест] Регистрация новго пользователя. (Взрослый котик)")

        val newUser = shokClient.registerUser(RegisterUser(
            emailAdult,
            passwordAdult,
            age = ageAdult))

        assertAll(
            {println("Закинули данные с новым пользователем.")},
            {assertThat(newUser.user.email).isEqualTo(emailAdult)},
            {println("Проверка произведена пользователь зарегистрирован: ${newUser}")}
        )
    }

    @Test
    @Order(6)
    fun existEmailAdultTestTrue(){
        println("\n[6 - Тест] Проерка наличия email Взрослый. (Зарегистрированный)")

        val existEmail = shokClient.existUser(ExistUserData(emailAdult))

        assertAll(
            {println("Email введен, ответ от сервера получен, сверяем.")},
            {assertThat(existEmail.exist).isEqualTo(true)}
        )
        println("Тест выполнен: результат проверки (шоковсти)- ${existEmail.exist}")
    }

    @Test
    @Order(7)
    fun loginAdultUserTrue(){
        println("\n[7 - Тест] Вход зарегистрированного пользователя.")

        val loginUser = shokClient.loginUser(UserLogIn(
            emailAdult,
            passwordAdult)
        )

        assertAll(
            {println("Проверка входа пользователя")},
            {assertThat(loginUser.user.email).isEqualTo(emailAdult)}
        )
        println("Тест выполнен: результат - ${loginUser.user.email}")
        println(loginUser)
        newAdultToken = loginUser.token
    }

    @Test
    @Order(8)
    fun newNameAdultUser(){
        println("\n[8 - Тест] Изменение имени пользователя")
        val name = randomName()
        val renameUser = shokClient.renameUser(
            UserName(name), newAdultToken)

        assertAll(
            {println("Проверка входа пользователя")},
            {assertThat(renameUser.user.name).isEqualTo(name)}
        )
        println("Тест выполнен: результат - ${renameUser.user.name}")
        println(renameUser)

    }

    @Test
    @Order(9)
    fun registerNewUserOld(){
        println("\n[9 - Тест] Регистрация новго пользователя. (Старый котик)")

        val newUser = shokClient.registerUser(RegisterUser(
            emailOld,
            passwordOld,
            age = ageOld))

        assertAll(
            {println("Закинули данные с новым пользователем.")},
            {assertThat(newUser.user.email).isEqualTo(emailOld)},
            {println("Проверка произведена пользователь зарегистрирован: ${newUser}")}
        )
    }

    @Test
    @Order(10)
    fun existEmailOldTestTrue(){
        println("\n[10 - Тест] Проерка наличия email старого котика. (Зарегистрированный)")

        val existEmail = shokClient.existUser(ExistUserData(emailOld))

        assertAll(
            {println("Email введен, ответ от сервера получен, сверяем.")},
            {assertThat(existEmail.exist).isEqualTo(true)}
        )
        println("Тест выполнен: результат проверки (шоковсти)- ${existEmail.exist}")
    }

    @Test
    @Order(11)
    fun loginUserTrue(){
        println("\n[11 - Тест] Вход зарегистрированного старого пользователя.")

        val loginUser = shokClient.loginUser(UserLogIn(emailOld, passwordOld))

        assertAll(
            {println("Проверка входа пользователя")},
            {assertThat(loginUser.user.email).isEqualTo(emailOld)}
        )
        println("Тест выполнен: результат - ${loginUser.user.email}")
        println(loginUser)
        newOldToken = loginUser.token
    }

    @Test
    @Order(12)
    fun newNameUser(){
        println("\n[12 - Тест] Изменение имени тсарого пользователя")
        val name = randomName()
        val renameUser = shokClient.renameUser(UserName(name), newOldToken)
        assertAll(
            {println("Проверка входа пользователя")},
            {assertThat(renameUser.user.name).isEqualTo(name)}
        )
        println("Тест выполнен: результат - ${renameUser.user.name}")
        println(renameUser)

    }

    @Test
    @Order(13)
    fun existEmailTestFalse(){
        println("\n[13 - Тест] Проерка наличия email. (НЕ зарегистрированный)")

        val existEmail = shokClient.existUser(ExistUserData(randomEmail()))

        assertAll(
            {println("Email введен, ответ от сервера получен, сверяем.")},
            {assertThat(existEmail.exist).isEqualTo(false)}
        )
        println("Тест выполнен: результат - ${existEmail.exist}")
    }

    @Test
    @Order(14)
    fun openApkNonLogout(){
        println("\n[14 - тест] Запуск приложения без логАут Yang пользователя")

        val userMe = shokClient.userMe(newYangToken)

        assertAll(
            {println("Запустил приложение молоденький котик. Ручка дернулась.")},
            {assertThat(userMe.user.email).isEqualTo(emailYang)}
        )
        println("Тест выполнен, автоматическое вхождение молоденьго котика. ${userMe}")
    }

    @Test
    @Order(15)
    fun openApkNonLogoutInvalToken(){
        println("\n[15 - тест] Запуск приложения без логАут с неверным токеном")
        val invalidToken = "invalid_token_123"

        val (stusCode, responsBody) = shokClient.userMeInvalid(invalidToken)

        assertAll(
            {println("Тест запущен, неверный токен улетел. Ждем результат.")},
            {assertEquals(401, stusCode)},
            {println("Полученный статус код сравнили с значением 401: рез. - $stusCode")},
            {assertThat(responsBody.message).isEqualTo("Invalid token")},
            {println("Сравнили результат, полученное сообщение: $responsBody")}
        )
    }

    @Test
    @Order(16)
    fun enterShockErrorPassword(){
        println("\n[16 - тест] Вход в приложение с неверным паролем")

        val (statuseCode, responsBody) = shokClient.errorLoginUser(UserLogIn(emailYang, randomErrorPassword()))

        assertAll(
            {println("Тест запущен, отправлен логин Молодого Котика, и пароль не соответсвующий ему")},
            {assertEquals(422, statuseCode)},
            {println("Полученный статус код сравнили со значением 422: рез. - $statuseCode")},
            {assertThat(responsBody.fields.password).isEqualTo("Неправильный логин или пароль")},
            {println("Сравнили результаты полученных ответов, сообщение: $responsBody")}
        )
    }




}