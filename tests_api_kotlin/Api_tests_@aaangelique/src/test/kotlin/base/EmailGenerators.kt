package ru.yavshok.tests.base

import kotlin.random.Random


object EmailGenerators {

    private val chars = ('a'..'z') + ('0'..'9')

    private val allowedChars = ('a'..'z') + ('0'..'9')
    // Рандомная строка заданной длины из allowedChars
    private fun randomString(length: Int): String =
        (1..length)
            .map { allowedChars.random() }
            .joinToString("")

    // Генерирует рандомный email в нижнем регистре с указанной длиной имени (без домена)
    fun generateEmail(length: Int = 10): String {
        val name = (1..length)
            .map { chars.random() }
            .joinToString("")
        return "$name@example.com"
    }

    // Генерирует рандомный email в верхнем регистре
    fun generateEmailUpperCase(length: Int = 10): String {
        return generateEmail(length).uppercase()
    }

    // Генерирует email с не-латинскими символами (например, кириллица)
    fun generateEmailNonLatin(): String {
        return "тест${Random.nextInt(100, 999)}@пример.рф"
    }

    // Генерирует email с двойной точкой в имени пользователя (невалидный)
    fun generateEmailWithDoubleDot(): String {
        val name = "user..test${Random.nextInt(10, 99)}"
        return "$name@example.com"
    }

    fun generateEmailWithLength(length: Int): String {
        require(length >= 7) { "Email length must be at least 7 chars" }

        val domain = "@e.com"
        val nameLength = length - domain.length
        val localPart = randomString(nameLength)

        return "$localPart$domain"
    }

    // Генерация email с спецсимволами
    fun generateEmailWithSpecialChars(valid: Boolean = true): String {
        return if (valid) {
            // Валидные спецсимволы: точка, плюс
            val localPart = randomString(5) + "." + randomString(3) + "+" + randomString(2)
            "$localPart@example.com"
        } else {
            // Невалидные спецсимволы: запятая, восклицательный знак
            val localPart = randomString(5) + "," + randomString(3) + "!" + randomString(2)
            "$localPart@example.com"
        }
    }



}