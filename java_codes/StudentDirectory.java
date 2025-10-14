import java.util.HashMap; //import necessary libraries
import java.util.Scanner; 

public class StudentDirectory{
    public static void main(String[] args){
        //Initialize the Scanner
        Scanner sc = new Scanner(System.in);
        HashMap<String, String> StudentList = new HashMap<>(); //Hash table

        System.out.print("How many students: ");
        int n = sc.nextInt(); //For number of students
        sc.nextLine();

        for(int i = 0; i < n; i++){
            System.out.print("Enter Student Number: ");
            String Studnum = sc.nextLine();

            System.out.print("Enter Student Name: ");
            String Studname = sc.nextLine();

            StudentList.put(Studnum, Studname);
        }
        System.out.println("Student Directory: " + StudentList);

        int choice;

        do {
            System.out.println("Operations \n1. Search 2. Remove 3. Add/Update 4. Exit");

            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1: //Searching
                    System.out.print("Enter the student number: ");
                    String searchnum = sc.nextLine();
                    
                    if (StudentList.containsKey(searchnum)){
                        System.out.println(searchnum + " - " + StudentList.get(searchnum));
                    } else{
                        System.out.println("Not Found");
                    }
                    break;
                case 2: //Remove
                    System.out.print("Enter the student number: ");
                    String removenum = sc.nextLine();

                    if (StudentList.containsKey(removenum)){
                        StudentList.remove(removenum);
                        System.out.println("Successfully removed");
                        
                    } else{
                        System.out.println("Invalid Input");
                    }
                    break;

                case 3:
                    System.out.print("Enter Student number: ");
                    String addnum = sc.nextLine();

                    System.out.print("Enter Student name: ");
                    String addname = sc.nextLine();

                    StudentList.put(addnum, addname);

                    System.out.println("Added Successfully"); 
                    break;               
                    
                case 4: //exit
                    System.out.println("Thank you");
                    break;

                default:
                    System.out.println("Invalid Input");
                    break;
            }
        } while(choice != 4);

        System.out.println("Updated Student Directory: " + StudentList);
    }
}