import java.util.Scanner;
public class Multiplication_Table {
    public static void main(String[] args){
        Scanner N = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int M = N.nextInt();
        System.out.println("\nMultiplication table of " + M);
        for(int i = 1; i <= 10; i++){
            System.out.println(i + " * " + M + " = " + (i * M));
        }
        N.close();

    }

}
