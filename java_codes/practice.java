import java.util.Scanner;

public class practice {
    public static void main(String[] args){
        //Create Scanner object
        Scanner scan = new Scanner(System.in);

        System.out.println("Operation: \n1. Summation \n2. Mean");
        System.out.print("Choice: ");
        int Choice = scan.nextInt();

        if (Choice < 0 || Choice > 2){ // && <- AND; || <- OR
            System.out.println("Invalid input");
        }
        else{

        if (Choice == 1){
            System.out.print("Enter the first number: ");
            int first = scan.nextInt();

            System.out.print("Enter the second number: ");
            int Second = scan.nextInt();
            
            Division(first, Second);
        }
        else if (Choice == 2){
            System.out.print("Enter how many numbers: ");
            int leng_num = scan.nextInt();

            float numbers[] = new float[leng_num]; //Initialize the array in Float datatype

            System.out.println("Enter the numbers: ");
            for(int i = 0; i < leng_num; i++){
                System.out.print(i+1+". ");
                numbers[i] = scan.nextFloat();
            }
            System.out.println("\nTotal Sum: " + Mean(numbers));
        }
    }

        //close the Scanner
        scan.close();
    }

    public static void Division(float x, float y){
        System.out.println("Result: " + (x/y));
    }

    public static float Mean(float[] x){
        float sum = 0;
        for(int i = 0; i < x.length; i++){
            sum = sum + x[i];
        }
        return sum;
    }
}
