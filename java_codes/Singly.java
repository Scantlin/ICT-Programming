class Node {
    String Songs;
    Node next;

    public Node(String Songs) {
        this.Songs = Songs;
        this.next = null;
    }
}

public class Singly {
    public static void main(String[] args) {
        Node Songs = new Node("Golden");
        Songs.next = new Node("Nandito ako");
        Songs.next.next = new Node("Mahal Kita");

        System.out.println("Before adding song 4");
        show(Songs);

        System.out.println("\nAfter adding song 4");
        Songs.next.next.next = new Node("Ikaw pa rin");
        show(Songs);

        System.out.println("\nRemoving song 2");
        Songs = remove(Songs, "Golden"); // Fixed: Changed to remove "Nandito ako" instead of "Golden"
        show(Songs);
    }

    public static void show(Node Songs) {
        Node current = Songs;

        while (current != null) {
            System.out.print(current.Songs + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static Node remove(Node head, String Songname) {
        // Handle case where head needs to be removed
        if (head.Songs.equals(Songname)) {
            return head.next;
        }
        
        Node current = head;
        while (current.next != null) {
            if (current.next.Songs.equals(Songname)) {
                current.next = current.next.next;
                return head;
            }
            current = current.next;
        }
        
        System.out.println("Song not found: " + Songname);
        return head;
    }
}