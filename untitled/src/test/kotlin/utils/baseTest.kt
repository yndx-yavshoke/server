package utils

import client.ShokClient
import io.restassured.RestAssured
import org.junit.jupiter.api.AfterAll
import org.junit.jupiter.api.BeforeAll
import java.time.LocalDateTime
import java.time.LocalTime

open class baseTest {

    companion object {
        lateinit var shokClient: ShokClient
        lateinit var startTime: LocalDateTime


        @BeforeAll
        @JvmStatic
        fun setup() {
            startTime = LocalDateTime.now()
            println("===Начало выполнения тестов===")
            RestAssured.enableLoggingOfRequestAndResponseIfValidationFails()
            shokClient = ShokClient()
        }

        @AfterAll
        @JvmStatic
        fun testDown() {
            val duration = java.time.Duration.between(startTime, LocalDateTime.now())
            println("\n=== Тесты завершены ===")
            println("Общее выполнение времени: ${duration.seconds} сек.")
        }
    }



}