import java.util.HashMap; //import necessary libraries
import java.util.Scanner; 

public class StudentDirectory{
    public static void main(String[] args){
        //Initialize the Scanner
        Scanner sc = new Scanner(System.in);
        HashMap<String, String> StudentList = new HashMap<>(); //Hash table contains String both key and Value

        System.out.print("How many students: ");
        int n = sc.nextInt(); //For number of students
        sc.nextLine(); //clear the enter key left in nextInt

        for(int i = 0; i < n; i++){
            System.out.print((i+1) + ". Enter Student Number: ");
            String Studnum = sc.nextLine(); //accept Student number

            System.out.print("Enter Student Name: ");
            String Studname = sc.nextLine(); //accept student name

            StudentList.put(Studnum, Studname); //add the given data to the hash table
        }
        System.out.println("\nStudent Directory: " + StudentList);

        int choice; //initialize int variable

        do {
            System.out.println("\nOperations \n1. Search 2. Remove 3. Add/Update 4. Exit");

            System.out.print("Enter your choice: "); //choice from user
            choice = sc.nextInt(); //get choice from user
            sc.nextLine(); //clear the enter key left in NextInt

            switch (choice) {
                case 1: //Searching
                    System.out.print("Enter the student number: ");
                    String searchnum = sc.nextLine();
                    
                    if (StudentList.containsKey(searchnum)){
                        System.out.println("Student Name: " + StudentList.get(searchnum));
                    } else{
                        System.out.println("Not Found");
                    }
                    break;
                case 2: //Remove
                    System.out.print("Enter the student number: ");
                    String removenum = sc.nextLine();

                    if (StudentList.containsKey(removenum)){
                        System.out.println("Successfully removed " + StudentList.get(removenum));
                        StudentList.remove(removenum); //remove the given if found
                        System.out.println("Updated Student Directory: " + StudentList); //show update
                    } else{
                        System.out.println("No Existing Record"); //return invalid if the user remove unexisting data
                    }
                    break;

                case 3: //for adding 
                    System.out.print("Enter Student number to add or update: ");
                    String newNum = sc.nextLine();

                    System.out.print("Enter Student name: ");
                    String newName = sc.nextLine();

                    if(StudentList.containsKey(newNum) && StudentList.containsValue(newName)){
                        System.out.println("Already Exist");
                    } else {
                        StudentList.put(newNum, newName);
                        System.out.println("No existing Record Found, Added/Updated entry");
                        System.out.println("Updated Student Directory: " + StudentList); //show update
                    }

                    break;               
                    
                case 4: //exit
                    System.out.println("Thank you");
                    break;

                default: //if user enter number not in menu
                    System.out.println("Invalid Input");
                    break;
            }
        } while(choice != 4); //condition to break the do-while loop
        sc.close(); //close the Scanner
    }
}