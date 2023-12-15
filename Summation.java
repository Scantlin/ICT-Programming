import java.util.Scanner;
class ain {
    public static void main(String[] args) {
        Scanner X = new Scanner(System.in);
        print("Enter a number of item to be added: ");
        int M = X.nextInt();
        double B [] = new double [M];

        print("Enter the numbers: \n");

        for(int i = 0; i < M; i++) {
            B[i] = X.nextDouble();
        }
        System.out.println("The sum of all number is " + sum(B));
        double xe = sum(B)/M;
        System.out.println("The mean is " + xe);

        X.close();
}

    static double sum(double numbers[]) {
        double sum = 0;
        for(double number: numbers) {
            sum = sum + number;
        }
        return sum;


}
    static void print(String word) {
        System.out.print(word);
    
    }
}