import com.github.javafaker.Faker;

public class DataHelper {
    private final Faker faker = new Faker();

    public User generateUser(){
        return User.builder()
                .email(email())
                .password(password())
                .age(age())
                .build();
    }

    private String email() {
        return faker.internet().emailAddress();
    }

    public String name() {
        return faker.name().firstName();
    }

    private String password() {
        return faker.internet().password(8, 16); // от 8 до 16 символов
    }

    private int age() {
        return faker.number().numberBetween(1, 99); // допустим, возраст от 18 до 80
    }
}

