import java.util.Scanner;

public class ThreadDemo extends Thread {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter your first thread: ");
        String name1 = scan.nextLine();

        System.out.print("Enter your second thread: ");
        String name2 = scan.nextLine();

        ThreadDemo first_Thread = new ThreadDemo();
        first_Thread.setName(name1);
        System.out.println(name1 + " is " + first_Thread.getState());

        ThreadDemo second_Thread = new ThreadDemo();
        second_Thread.setName(name2);
        System.out.println(name2 + " is " + second_Thread.getState());

        System.out.println("\nStarting the thread");
        first_Thread.start();

        try {
            first_Thread.join(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        second_Thread.start();

        try {
            second_Thread.join();
            System.out.println("\nTerminated phase:"); // Added message before terminated status
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println(first_Thread.getName() + " is TERMINATED.");
        System.out.println(second_Thread.getName() + " is TERMINATED.");
    }


    public void run() {
        System.out.println(Thread.currentThread().getName() + " is RUNNABLE.");
        try {
            Thread.sleep(3000); // suspends thread for 3 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}