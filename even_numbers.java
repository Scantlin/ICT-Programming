import java.util.Scanner;
public class even_numbers {
    public static void main(String[] args){
        Scanner N = new Scanner(System.in);
        int x = 2;
        int w = 3;
        System.out.print("Enter how many even numbers you need: ");
        int m = N.nextInt();
        System.out.print("Enter how many odd number: ");
        int we = N.nextInt();
        System.out.println("Even numbers:");
        for(int i = 1;i <= m; i++ ){
            System.out.println(i * x);
        }
        System.out.println("Odd numbers:");
        for(int i = 1; i <= we; i++){
            System.out.println(i * w);
        }
        N.close();
    }
    
}
