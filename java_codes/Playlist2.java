import java.util.Scanner;

// Node class
class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// LinkedList class
class LinkedList {
    Node head;

    // Insert data at the end
    public void insert(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
        System.out.println(data + " inserted successfully.");
    }

    // Delete node by value
    public void delete(int data) {
        if (head == null) {
            System.out.println("List is empty.");
            return;
        }

        // If head node is the one to be deleted
        if (head.data == data) {
            head = head.next;
            System.out.println(data + " deleted successfully.");
            return;
        }

        Node current = head;
        Node prev = null;

        // Traverse the list to find the node to delete
        while (current != null && current.data != data) {
            prev = current;
            current = current.next;
        }

        // If data not found
        if (current == null) {
            System.out.println(data + " not found in the list.");
            return;
        }

        // Delete the node
        prev.next = current.next;
        System.out.println(data + " deleted successfully.");
    }

    // Display the list
    public void display() {
        if (head == null) {
            System.out.println("List is empty.");
            return;
        }

        Node current = head;
        System.out.print("Linked List: ");
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}

// Main class
public class Playlist2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList list = new LinkedList();
        int choice, value;

        while (true) {
            System.out.println("\n--- Linked List Menu ---");
            System.out.println("1. Insert");
            System.out.println("2. Delete");
            System.out.println("3. Display");
            System.out.println("4. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter value to insert: ");
                    value = sc.nextInt();
                    list.insert(value);
                    break;
                case 2:
                    System.out.print("Enter value to delete: ");
                    value = sc.nextInt();
                    list.delete(value);
                    break;
                case 3:
                    list.display();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    sc.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice. Try again.");
            }
        }
    }
}