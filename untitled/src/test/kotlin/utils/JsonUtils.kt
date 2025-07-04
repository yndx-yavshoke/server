package utils

import kotlinx.serialization.SerializationException
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import kotlinx.serialization.serializer

object JsonUtils {
    val json = Json{
        ignoreUnknownKeys = true
        isLenient = true
        encodeDefaults = true
        prettyPrint = true
    }

    inline fun <reified T> toJson(obj: T): String {
        return json.encodeToString(serializer(), obj)
    }

    inline fun <reified T> fromJson(jsonString: String): T {
        return try {
            json.decodeFromString(jsonString)
        } catch (e: SerializationException) {
            println("Вот строчка: $jsonString")
            throw RuntimeException("Ошибка при парсе данных JSON")
        }
    }
}