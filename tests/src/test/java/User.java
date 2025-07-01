import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data                   // генерирует геттеры/сеттеры, toString, equals и hashCode
@NoArgsConstructor      // пустой конструктор
@AllArgsConstructor     // конструктор со всеми полями
@Builder
public class User {
    private String token;
    private String email;
    private String name;
    private String password;
    private int age;
}
