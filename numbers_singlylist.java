import java.util.Scanner;

class Node {
    int number;
    Node next;

    public Node(int number) {
        this.number = number;
        this.next = null;
    }
}

public class numbers_singlylist {
    static Node data = null;

    public static void show() {
        if (data == null) {
            System.out.println("The list is empty!");
            return;
        }

        Node current = data;
        while (current != null) {
            System.out.print(current.number + ", ");
            current = current.next;
        }
        System.out.println("Null");
    }

    public static void add(int value) {
        Node newNode = new Node(value);
        
        if (data == null) {
            data = newNode;
        } else {
            Node current = data;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
        System.out.println("Added: " + value);
    }

    public static void deleteNode(int value) {
        if (data == null) {
            System.out.println("Cannot delete " + value + " - The list is empty!");
            return;
        }

        // Handle case where head node needs to be deleted
        if (data.number == value) {
            data = data.next;
            System.out.println("Deleted: " + value);
            return;
        }

        // Traverse the list to find the node to delete
        Node current = data;
        while (current.next != null) {
            if (current.next.number == value) {
                current.next = current.next.next;
                System.out.println("Deleted: " + value);
                return;
            }
            current = current.next;
        }

        // If we reach here, the value was not found
        System.out.println("Cannot delete " + value + " - Value not found in the list!");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        
        do {
            System.out.println("\n=== NUMBER LIST MENU ===");
            System.out.println("1. Insert Number");
            System.out.println("2. Delete a Number");
            System.out.println("3. Show the List");
            System.out.println("4. Exit");
            System.out.print("Enter your choice (1-4): ");
            
            choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    System.out.print("Enter number to insert: ");
                    int num1 = scanner.nextInt();
                    add(num1);
                    break;
                    
                case 2:
                    if (data == null) {
                        System.out.println("The list is empty! Nothing to delete.");
                    } else {
                        System.out.print("Enter number to delete: ");
                        int num2 = scanner.nextInt();
                        deleteNode(num2);
                    }
                    break;
                    
                case 3:
                    System.out.println("\nCurrent List:");
                    show();
                    break;
                    
                case 4:
                    System.out.println("Exiting program. Goodbye!");
                    break;
                    
                default:
                    System.out.println("Invalid choice! Please enter a number between 1-4.");
            }
            
        } while (choice != 4);
        
        scanner.close();
    }
}