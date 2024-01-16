import java.util.Scanner;
public class Game {
    static String answers [] = {"jupiter", "mars", "Earth"};

    public static void main(String[] args){
        Scanner X = new Scanner(System.in);
        System.out.println("Welcome to our game");
        print("You have 3 lives, you to need have a perfect score to win");
        int i = 3;
        while (i > 0) {
            print("\n1. What is the fifth planet in our solar system: ");
            String in1 = X.nextLine();
            print("2. Also known as red planet: ");
            String in2 = X.nextLine();
            print("3. Habitable planet: ");
            String in3 = X.nextLine();
            
            if (in1.equalsIgnoreCase(answers[0]) && in2.equalsIgnoreCase(answers[1]) && in3.equalsIgnoreCase(answers[2])) {
                System.out.println("You've got all the answers correct");
                break;
            } else if(in1.equalsIgnoreCase(answers[0]) && in2.equalsIgnoreCase(answers[1])) {
                System.out.print("You've got 2 correct answers");
                i--;
                if (i > 0) print("\ntry again");
            } else if (in2.equalsIgnoreCase(answers[1]) && in3.equalsIgnoreCase(answers[2])) {
                System.out.print("You've got 2 correct answers");
                i--;
                if (i > 0) print("\ntry again");
                
            } else if (in1.equalsIgnoreCase(answers[0])) {
                System.out.print("Got one right answer");
                i--;
                if (i > 0) print("\ntry again");
            } else if (in2.equalsIgnoreCase(answers[1])) {
                System.out.print("Got one right answer");
                i--;
                if (i > 0) print("\ntry again");
            } else if (in3.equalsIgnoreCase(answers[2])) {
                print("Got one right answer");
                i--;
                if (i > 0) print("\ntry again");
            } else if (in1.equalsIgnoreCase(answers[0]) && in3.equalsIgnoreCase(answers[2])) {
                print("Got two correct answer");
                i--;
                if (i > 0) print("\ntry again");
            } else {System.out.print("None correct answer"); 
        i--;
        if (i > 0) print("\ntry again");
    }
        } if (i > 0) {
            print("You won, Congratulations!!");
        } else print("\nout of lives, YOU LOST");
        X.close();
    }
    static void print(String word){
        System.out.print(word);

    }
}
