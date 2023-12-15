import java.util.Scanner;
public class Game2 {
    static String answer [] = {"Crust", "Mantle", "Core"};
    public static void main(String[] args) {
        Scanner M = new Scanner(System.in);
        print("Welcome to the game \n");
        print("You have three lives and need to answer three questions. You need a perfect score to win");
        int i = 3;
        int x = 0;
        while(i > 0) {
            print("\nWhat is the 1st layer of earth? ");
            String me = M.nextLine();
            print("What is the second layer of earth? ");
            String om = M.nextLine();
            print("Third layer of earth? ");
            String o = M.nextLine();

            if(me.equalsIgnoreCase(answer[0])) {
                x++;
            }
            if(om.equalsIgnoreCase(answer[1])) {
                x++;
            }
            if (o.equalsIgnoreCase(answer[2])) {
                x++;
            }

            switch(x) {
                case 3:
                print("Congratulations! You got all three questions right!");
                i=0;
                break;
                case 2:
                print("You got 2 correct answer");
                i--;
                x=0;
                if(i > 0) print("\nTry again");
                break;
                case 1:
                print("you got 1 correct answer");
                i--;
                x=0;
                if(i > 0) print("\nTry again");
                break;
                default: print("None of your answer is correct");
                i--;
                if(i > 0) print("\nTry again");
                break;
            }
        } System.out.println("\nYou Lost!!");
        M.close();

    }
    static void print(String word) {
        System.out.print(word);
    }
}
