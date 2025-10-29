// Import necessary tools (libraries) we need for the program
import java.util.HashMap;      // For storing data in key-value pairs
import java.util.HashSet;      // For storing unique items
import java.util.Map;          // Interface for key-value collections
import java.util.Queue;        // For first-in-first-out data structure
import java.util.List;         // For ordered collections
import java.util.ArrayDeque;   // For efficient queue implementation
import java.util.ArrayList;    // For resizable arrays
import java.util.Set;          // Interface for unique item collections
import java.util.Collections;  // Utility methods for collections
import java.util.Scanner;      // For reading user input

public class CampusWayFinder {
    // Inner class to represent our graph (map of locations and connections)
    static class Graphs{
        // This stores our graph data: each location and its connected locations
        private final Map<String, List<String>> adj = new HashMap<>();
    
        // Method to connect two locations (add an edge between them)
        public void addEdge(String u, String v){
            // Add v to u's list of neighbors, creating list if it doesn't exist
            adj.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
            // Add u to v's list of neighbors (makes it a two-way connection)
            adj.computeIfAbsent(v, k -> new ArrayList<>()).add(u);
        }
        
        // Method to display all locations and their connections
        public void printAdjacency(){
            // Go through each location in our map
            for(var entry: adj.entrySet()){
                // Print location -> [list of connected locations]
                System.out.println(entry.getKey() + " -> " + entry.getValue());
            }
        }
        
        // Depth First Search - explores as far as possible along each branch
        void dfs(String u, Set<String> visited){
            visited.add(u);          // Mark current location as visited
            System.out.print(u + " "); // Print current location

            // Check all neighbors of current location
            for (String v : adj.getOrDefault(u, List.of())) {
                // If neighbor hasn't been visited yet
                if (!visited.contains(v)){
                    dfs(v, visited); // Recursively visit that neighbor
                }
            }
        }

        // Breadth First Search - finds shortest path between two locations
        void bfs(String start, String target) {
            // If start and target are the same location
            if (start.equals(target)) {
                System.out.println("Start and target are the same: " + start);
                return;
            }
            
            // Check if both locations exist in our map
            if (!adj.containsKey(start) || !adj.containsKey(target)) {
                System.out.println("No path exists from " + start + " to " + target + " (vertex not found)");
                return;
            }
            
            // Setup for BFS:
            Map<String, String> parent = new HashMap<>(); // Tracks how we reached each location
            Set<String> visited = new HashSet<>();        // Tracks visited locations
            Queue<String> queue = new ArrayDeque<>();     // Queue for BFS traversal
            
            visited.add(start);  // Mark start as visited
            queue.add(start);    // Add start to queue
            parent.put(start, null); // Start has no parent (it's the beginning)
            
            boolean found = false; // Flag to track if we found the target
            
            // Continue searching while there are locations to check and target not found
            while (!queue.isEmpty() && !found) {
                String current = queue.poll(); // Get next location from queue
                
                // Check all neighbors of current location
                for (String neighbor : adj.getOrDefault(current, List.of())) {
                    if (!visited.contains(neighbor)) {
                        visited.add(neighbor);        // Mark neighbor as visited
                        parent.put(neighbor, current); // Record how we got to neighbor
                        queue.add(neighbor);          // Add neighbor to queue for later checking
                        
                        // If we found our target location
                        if (neighbor.equals(target)) {
                            found = true;  // Set flag to true
                            break;         // Exit the loop
                        }
                    }
                }
            }
            
            // If we found a path, reconstruct and display it
            if (found) {
                List<String> path = reconstructPath(parent, start, target);
                System.out.println("Shortest path from " + start + " to " + target + ": " + path);
            } else {
                System.out.println("No path exists from " + start + " to " + target);
            }
        }
        
        // Helper method to build the path from start to target
        private List<String> reconstructPath(Map<String, String> parent, String start, String target) {
            List<String> path = new ArrayList<>();
            String current = target;  // Start from the target
            
            // Work backwards from target to start using parent information
            while (current != null) {
                path.add(current);           // Add current location to path
                current = parent.get(current); // Move to parent (how we got here)
            }
            
            // Reverse the path so it goes from start to target
            Collections.reverse(path);
            return path;
        }
        
    }
    
    // Main method - where program execution begins
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);  // Create scanner for user input
        Graphs g = new Graphs();                // Create object for Graph

        g.addEdge("A", "B");  // Connect A to B
        g.addEdge("A", "C");  // Connect A to C  
        g.addEdge("B", "D");  // Connect B to D
        g.addEdge("C", "D");  // Connect C to D

        // Display all locations and their connections
        System.out.println("Adjacency List:");
        g.printAdjacency();

        // Get user input for DFS starting point
        System.out.print("\nEnter start vertex for DFS: ");
        String dfs_SV = scan.nextLine();

        // Perform DFS and show traversal order
        System.out.print("DFS order: ");
        g.dfs(dfs_SV, new HashSet<>());
        
        // Get user input for path finding
        System.out.print("\n\nEnter start and target vertices: ");
        String bfs_ST = scan.nextLine();

        // Split input into start and target locations
        String[] vertices = bfs_ST.split(" ");
        String bfs_SV = vertices[0];  // Start location
        String bfs_TV = vertices[1];  // Target location

        // Find and display shortest path
        g.bfs(bfs_SV, bfs_TV);
        scan.close(); 
    }
}