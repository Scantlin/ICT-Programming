//import necessary libraries/classes to use in our activities
import java.util.PriorityQueue; //for min heap
import java.util.Collections; //for max heap
import java.util.Scanner; //to get the value from user

public class HeapLab {
    public static void main(String[] args) { //main method
        Scanner sc = new Scanner(System.in); //object for Scanner with sc being named of it

        System.out.print("Enter the number of incidents: ");
        int n = sc.nextInt();
        sc.nextLine(); //to clear to leftover enter key from input n
        
        int[] ids = new int[n]; //array of ids
        String[] locations = new String[n]; //array of Locations
        int[] severities = new int[n]; //array for severities

        PriorityQueue<Integer> minHeap = new PriorityQueue<>(); //For Minheap
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder()); //for Maxheap

        //inputting the incident location and severity using loop according to the input of user
        for(int i = 0; i < n; i++){
            ids[i] = 101 + i;

            System.out.print(ids[i]  + " - Location: ");
            locations[i] = sc.nextLine(); //assign the input locations to an array using indexing

            System.out.print(ids[i] + " - Severity (1-10): ");
            severities[i] = sc.nextInt(); //assign the input severity to an array of severities using indexing
            sc.nextLine(); //to clear leftover

            minHeap.add(severities[i]); //adding to max heap
            maxHeap.add(severities[i]); //adding to min heap
        }

        //Dispatch Order (Max-heap)
        int sev_auth = 0; //this is to avoid duplication once there are similar priorities

        System.out.println("\nDispatch Order (Max-Heap)");
        while (!maxHeap.isEmpty()){ //looping maxHeap while it is not empty
        int sev = maxHeap.poll(); //get the highest Severity

        if (sev != sev_auth){ //Comparing first if a priority is equivalent to previous priority to avoid duplication
        for (int i = 0; i < n; i++){ //loop for checking one by one the element in array of severities
            if (severities[i] == sev){ //compare one by one element using indexing to the severities that the maxHeap return
                System.out.println(ids[i] + " - " + locations[i] + " (Severitity: " + severities[i] + ")"); //Will get the output
            }
        }
        sev_auth = sev; //assigned the current value of sev to sev_auth to do comparison
    }
}
        //Backlog monitoring using the Minheap
        sev_auth = 0;
        System.out.println("\nBacklog Monitoring (Min-Heap)");
        while(!minHeap.isEmpty()){
            int sev = minHeap.poll(); //return the lowest severity

            if (sev_auth != sev){ //avoid duplication
            for (int i = 0; i < n; i++){
                if (severities[i] == sev){
                    System.out.println(ids[i] + " - " + locations[i] + " (Severity: " + severities[i] + ")");
            }
        }
        sev_auth = sev; //assign the current sev to sev_auth will be the previous sev
    }
    }
        sc.close(); //always close the Scanner
}
}
