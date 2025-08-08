import java.util.ArrayList;

public class sample {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(5);
        numbers.add(10);
        System.out.println("Dynamic Array Elements");

        for (int number: numbers){
            System.out.println(number);
        }
    }
}