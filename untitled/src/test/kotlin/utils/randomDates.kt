package utils

import kotlin.random.Random


fun randomEmail(): String{
    val domain = "ya.ru"
    val length = Random.nextInt(5, 15)
    val username = (1..length)
        .map { ('a'..'z').random() }
        .joinToString("")

    return "$username@$domain"
}

fun randomPassword(): String{
    val chars = "QWERTYUIOPASDFGHJKLZXCVBNM" +
            "qwertyuiopasdfghjklzxcvbnm" +
            "1234567890!@#$%^&*()-+=_"
    return (1..Random.nextInt(5, 21))
        .map { chars.random()}
        .joinToString("")
}

fun randomAge(people: String): Int{
    return when (people) {
        "yang" -> Random.nextInt(0, 22)
        "adult" -> Random.nextInt(22, 69)
        else -> Random.nextInt(69, 100)
    }
}

fun randomName(): String{
    val names: List<String> = listOf("Serg", "Serg152", "Сергей", "Сергей🔥",
        "谢尔盖", "سيرجي", "सर्गेई", "セルゲイ・イワノビッチ", "谢尔盖 (Sergey)")
    return names.random()
}

fun randomErrorPassword(): String{
    val passwords: List<String> = listOf("", "1", "12", "123", "1234", "123456789012345678901", "1qa!2ws@3ed#4rf$5tg%")
    return passwords.random()
}

fun randomErrorEmail(): String {
    val errorEmail: List<String> = listOf("user.example.com", "test#gmail.com", "hello.world", "@example.com", "user@",
        "user@.com", "user@example..com", "user name@example.com", "user@example",
        "this.is.a.very.very.long.email.address.that.exceeds.fifty.chars@example.com")
    return errorEmail.random()
}