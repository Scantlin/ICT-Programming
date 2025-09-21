import java.util.Scanner;   
public class switch_statement{
    public static void main(String[] args){
        Scanner Scan = new Scanner(System.in); //Object for Scanner

        System.out.println("Enter the numbers: ");
        int First_num = Scan.nextInt();
        int Second_num = Scan.nextInt();

        System.out.println("Enter your Operation");
        String operation = Scan.next();

        switch(operation){
            case "sum":
                System.out.println("Addition: " + (First_num + Second_num));
                break;
            case "Subtract":
                System.out.println("Differences: " + (First_num - Second_num));
                break;
            case "division":
                try{
                    System.out.println("Division: " + (First_num / Second_num));
                }
                catch(Exception e){
                    System.out.println("There is an error");
                }
                break;
            case "multiplication":
                System.out.println("Multiply: " + (First_num * Second_num));
                break;
            default:
                System.out.println("Invalid Operation");
        }

        //Close the Scanner
        Scan.close();
    }
}