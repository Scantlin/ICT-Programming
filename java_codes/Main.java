//import necessary classes to be use
import java.util.PriorityQueue; //To Create Heaps 
import java.util.Comparator; //Use for controlling how task are ordered
import java.util.Scanner; //To get input from the user

class Task{ //A class for Task
    String description;
    int priority;
    
    Task(String description, int priority){ //Constructor that accepts two parameters
        this.description = description;
        this.priority = priority;
    }

    @Override
    public String toString(){ //Method to define how each task will be displayed when printed
        return "[Priority " + priority + "] " + description;
    }
}
//Main Class
public class Main {
    public static void main(String[] args) { //main Method
        Scanner sc = new Scanner(System.in); //object of Scanner 

        //declaring priority queue
        PriorityQueue<Task> taskQueue = new PriorityQueue<>(Comparator.comparingInt((Task t) -> t.priority).reversed());

        System.out.print("Enter number of Task: ");
        int n = sc.nextInt();//input how many tasks from user
        sc.nextLine(); //To clear leftover from int n

        for(int i = 0; i < n; i++){
            System.out.print("Enter the description: for task " + (i + 1) + ": ");
            String desc = sc.nextLine(); //Assign the input of user to desc and it was repeating 

            System.out.print("Enter the priority (1-10) for task " + (i + 1) + ": ");
            int prio = sc.nextInt(); //Assign the input of user to desc and it was repeating

            taskQueue.add(new Task(desc, prio)); //adding the desc and prio to the heaps
            sc.nextLine(); //Clearing leftover from the two inputs
        }

        System.out.println("\nNext Task: " + taskQueue.peek()); //checking the highest priority without removing it to the Queue
        
        System.out.println("\nProcessing tasks in order of priority");

        while(!taskQueue.isEmpty()){ //keep processing tasks while queue is not empty
            System.out.println(taskQueue.poll()); //printing the Queue descending order
        }
        if (taskQueue.isEmpty()){ //check if the Queue is empty and proceed to responding actions once True
            System.err.println("\nAll Tasks have been processed");
        }

        sc.close(); //Close the Scanner
    }
}
