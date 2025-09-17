import java.util.Scanner;

public class For_Array{
    public static void main(String[] args) {
        Scanner Scan = new Scanner(System.in);

        //With Values
        int numbers[] = {1, 2, 3, 4, 5};
        int sum = 0;

        for(int x = 0; x < numbers.length; x++){
            sum = numbers[x] + sum;
        }
        System.out.println("summation: " + sum);

        //Without Values
        System.out.print("Enter the length of array: ");
        int number_input = Scan.nextInt();

        String names[] = new String[number_input + 1];

        System.out.println("Enter the names: ");
        for(int x = 0; x <= number_input; x++){
            names[x] = Scan.nextLine();   
        }

        System.out.println("Names: ");

        for(int y = 0; y < names.length ; y++){
            System.out.println(names[y]);
        }

        Scan.close();
    }
}