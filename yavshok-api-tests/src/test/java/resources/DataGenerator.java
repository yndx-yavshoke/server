package resources;

import java.util.*;

public class DataGenerator {
    public static String generateUniqueEmail() {
        return "user" + UUID.randomUUID().toString() + "@yandex.ru";
    }

    public static int youngCat(){
        Random rndNumber= new Random();
        return rndNumber.nextInt(21);
    }

    public static int adultCat(){
        Random rndNumber= new Random();
        return rndNumber.nextInt(22,68);
    }

    public static int oldCat(){
        Random rndNumber= new Random();
        return rndNumber.nextInt(69,99);
    }
}
