import java.util.Scanner;
public class Basic_Calcu {
    public static void main(String[] args){
        Scanner M = new Scanner(System.in);
        print("List of calculator \n" + "1. Quadratic Calcu \n" + "2. Find the Square root \n" );
        print("Enter your choice: ");
        int choice = M.nextInt();

        if (choice == 1) {
            print("This is quadratic Calculator \n" + "Enter the coefficient of x²: ");
            double a = M.nextDouble();
            print("Enter the coefficient of x: ");
            double b = M.nextDouble();
            print("Enter the constant: ");
            double c = M.nextDouble();
            Quadratic(a, b, c);
        }
        else if (choice == 2) {
            print("Please enter the number for which you would like to find the square root: ");
            double Xe = M.nextDouble();
            Square(Xe);
        } else print("Invalid Command");

        M.close();
    }
    static void Quadratic(double x, double m, double i){
        double z [] = {4*x*i, Math.pow(m, 2),2*x};
        double mz = z[1] - z[0];
        double ee = Math.sqrt(mz);
        double xs = -m;
        System.out.println("The first root is " + (xs - ee)/z[2]);
        System.out.println("The second root is " + (xs + ee)/z[2]);
    }
    static double Square(double x) {
        return Math.sqrt(x);
    }
    static void print(String word){
        System.out.print(word);
    }
}