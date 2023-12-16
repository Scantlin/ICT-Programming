import java.util.Scanner;
public class Reverse_name {
    public static void main(String[] args) {
        Scanner X = new Scanner(System.in);
        boolean go = true;
        while (go) {
        System.out.print("Enter original word: ");
        String original = X.nextLine();
        StringBuilder reversed = new StringBuilder(original).reverse();
        System.out.println("Original: " + original);
        System.out.println("Reversed: " + reversed.toString());
        print("Continue?\n" + "1. Yes\n" + "2. No\n");
        print("Enter your choice: ");
        int choice = X.nextInt();
        if (choice == 1) {
            print("Okie");
        } else if (choice == 2) {
            print("Thank you");
            go = false;
        }
        else print("Invalid command\n");

        }
        X.close();
    }
    static void print(String word){
        System.out.print(word);
    }
}
