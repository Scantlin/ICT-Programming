//import necessary libraries
import java.util.HashSet; //for hashset
import java.util.Scanner; //for Scanner
import java.util.HashMap; //for Hashmap

public class Hashset {
    public static void main(String[] args) {
        System.out.println("====== HASHSET ====== \n");
        HashSet<String> courses = new HashSet<>(); //Empty Hashset named courses
        Scanner scan = new Scanner(System.in); //Initialize Scanner

        for(int i = 0; i < 4; i++){ //looping to accept 4 courses
            System.out.print("Enter Course " + (i+1) + ": ");
            String course = scan.nextLine();
            courses.add(course); //to add the course inputted by the user to the HashSet
        }

        System.out.println("Courses: " + courses + "\n"); //print all the courses in Hashset

        System.out.print("Search Course: "); 
        String SearchCourse = scan.nextLine(); //Courses to search

        if(courses.contains(SearchCourse)){ //conditions to check if the inputted to search exist or not
            System.out.println(SearchCourse + " is available");
        } else{
            System.out.println(SearchCourse + " is not available");
        }

        System.out.print("Remove course: ");
        String RemoveCourse = scan.nextLine();

        if(courses.contains(RemoveCourse)){
            courses.remove(RemoveCourse); //remove the course inputted
            System.out.println("Courses after removal: " + courses);
        } else{
            System.out.println(RemoveCourse + " is not exist");
        }

        System.out.println("\n===== HASHMAP =====\n");

        HashMap<String, Integer> grades = new HashMap<>(); //initialize hashmap

        for(int i =0; i < 3; i++){ //looping to enter the 3 students
            System.out.print("Enter Student " + (i+1) + " name: ");
            String name = scan.nextLine();
            System.out.print("Enter " + name + "'s grade: ");
            int grade = scan.nextInt();

            grades.put(name, grade); //put the data into the Hashmap
            scan.nextLine(); //clear the enter key left in nextint
        }

        System.out.println("Grades: " + grades + "\n"); //print all the grades in Hashmap
        
        //For Search
        System.out.print("Search student: ");
        String SearchStudent = scan.nextLine(); //Enter student to search

        if(grades.containsKey(SearchStudent)){ //if enter was found
            System.out.println(SearchStudent + "'s grade: " + grades.get(SearchStudent));
        }
        else{
            System.out.println(SearchStudent + " is not exist");
        }

        //For update
        System.out.print("Update Student: ");
        String UpdateStudent = scan.nextLine(); 

        if(grades.containsKey(UpdateStudent)){ //if exist
            System.out.print("New grade: ");
            int newGrade = scan.nextInt();

            grades.remove(UpdateStudent);
            grades.put(UpdateStudent, newGrade);

            System.out.println("Grades after update: " + grades);
            scan.nextLine();
        }
        else{ //if not
            System.out.println(UpdateStudent + " is not exist");
        }

        //For Remove
        System.out.print("Remove student: ");
        String RemoveStudent = scan.nextLine(); //accept student to remove

        if(grades.containsKey(RemoveStudent)){ //if enter is exist or in a Hashmap
            grades.remove(RemoveStudent);
            System.out.println("Grades after removal " + grades);
        } else { //if not
            System.out.println(RemoveStudent + " is not exist");
        }

        scan.close(); //close the Scanner
    }
    
}