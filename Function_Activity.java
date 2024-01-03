import java.util.Scanner;
class Summation {
    public static void main(String[] args) {
        Scanner X = new Scanner(System.in);
        print("Enter the total item: ");
        int re = X.nextInt();
        double sm[] = new double[re];

        print("Enter the numbers: " + "\n");
        for(int i = 0; i < re; i++) {
            sm[i] = X.nextDouble();
                }

        double t = Sum(sm);
        double mt = t/sm.length;
        System.out.println("The sum of all item is " + t + "\n" + "The mean is " + mt);

        if (mt >= 98 ) System.out.println("With highest honor");
        else if (mt >= 95) System.out.println("With high honor");
        else if (mt >= 90) System.out.println("With honor");
        else System.out.println("Better Luck next time");
            }

    static double Sum(double numbers[]) { //a function for summation
        double sum = 0;
        for (double number : numbers) {
            sum = sum + number;
        }
        return sum/ numbers.length;
    }
    static void print(String word) {
        System.out.print(word);
    }
}