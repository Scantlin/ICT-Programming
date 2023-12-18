import java.util.Scanner;
public class Diamond {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of rows (odd): ");
        int rows = scanner.nextInt();

        if (rows % 2 == 0) {
            System.out.println("Please enter an odd number for a symmetric diamond pattern.");
            return;
        }

        int spaces = rows / 2;

        // Upper part of the diamond
        for (int i = 1; i <= rows; i += 2) {
            for (int j = 0; j < spaces; j++) {
                System.out.print(" ");
            }

            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }

            System.out.println();
            spaces--;
        }

        // Lower part of the diamond
        spaces = 1;
        for (int i = rows - 2; i >= 1; i -= 2) {
            for (int j = 0; j < spaces; j++) {
                System.out.print(" ");
            }

            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }

            System.out.println();
            spaces++;
        }

        scanner.close();
    }
}

