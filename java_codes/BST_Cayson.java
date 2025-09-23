import java.util.InputMismatchException;
import java.util.Scanner;

// BST Node class
class BSTNode {
    int key;
    BSTNode left, right;
    
    // Constructor that accepts an int parameter named key
    public BSTNode(int key) {
        this.key = key;
        this.left = null;
        this.right = null;
    }
}

// Binary Search Tree class
class BST {
    BSTNode root; //BSTNode Variable named root
    
    public BST() {
        root = null;
    }
    
    // Insertion using recursion
    public void insert(int key) {
        root = insertRec(root, key);
    }
    
    private BSTNode insertRec(BSTNode n, int k) {
        // If the tree is empty, create a new node
        if (n == null) {
            return new BSTNode(k);
        }
        
        // Otherwise, recur down the tree
        if (k < n.key) {
            n.left = insertRec(n.left, k);
        } else if (k > n.key) {
            n.right = insertRec(n.right, k);  // FIXED: Changed root.right to n.right
        }
        
        // Return the (unchanged) node pointer
        return n;
    }
    
    public boolean search(BSTNode n, int k) {
        // Base cases: root is null or key is present at root
        if (n == null) {
            return false; //Since the return should be boolean
        }
        
        if (n.key == k) {
            return true;
        }
        
        // Key is greater than root's key
        if (k < n.key) {
            return search(n.left, k);
        }
        
        // Key is smaller than root's key
        return search(n.right, k);
    }
    
    // Deletion using recursion
    public void delete(int key) {
        root = deleteRec(root, key);
    }
    
    private BSTNode deleteRec(BSTNode n, int k) {
        // Base case: tree is empty
        if (n == null) {
            return null;
        }
        
        // Recur down the tree
        if (k < n.key) {
            n.left = deleteRec(n.left, k);
        } else if (k > n.key) {
            n.right = deleteRec(n.right, k);
        } else {
            // Node with only one child or no child
            if (n.left == null) {
                return n.right;
            } else if (n.right == null) {
                return n.left;
            }
            
            // Node with two children: get the inorder successor (smallest in right subtree)
            n.key = minValue(n.right);
            
            // Delete the inorder successor
            n.right = deleteRec(n.right, n.key);
        }
        
        return n;
    }
    
    private int minValue(BSTNode n) { //method that returns int and accept BSTNode
        while (n.left != null) {
            n = n.left;
        }
        return n.key;
    }
    
    // Inorder traversal using recursion
    public void InorderPrint() {
        inorder(root); //Call for helper method
        System.out.println(); //Move the next cursor to the next line
    }
    
    private void inorder(BSTNode n) { //Helper method
        if (n != null) {
            inorder(n.left);
            System.out.print(n.key + " ");
            inorder(n.right);
        }
    }
    
}

// Main class to test the BST implementation
public class BST_Cayson {
    public static void main(String[] args) {

        //Scanner Object
        Scanner scan = new Scanner(System.in);

        BST t = new BST(); // Object of BST that named t

        int[] vals = new int[5]; //create an array containing the values (elements)
        
        // Insert elements using for loops
        System.out.println("Enter values: ");

        try{
            for (int i = 0; i < vals.length; i++){
                vals[i] = scan.nextInt();
                t.insert(vals[i]);
                }
        }
        
        catch(InputMismatchException e){
            System.out.println("Wrong input");
        }

        finally {
        System.out.print("\nInputted Values: ");
        for (int i = 0; i < vals.length; i++){
            System.out.print(vals[i] + " ");
        }
        // Print inorder traversal
        System.out.print("\nInorder traversal: ");
        t.InorderPrint();
        
        // Search for elements sample 40 and 120
        System.out.println("\nSearching operations:");

        //for #40
        if (t.search(t.root, 40)){
            System.out.println("Search 40: Found");
        } else{
            System.out.println("Search 40: Not Found");
        }

        //for #100
        if (t.search(t.root, 100)){
            System.out.println("Search 100: Found");
        }
        else{
            System.out.println("Search 100: Not Found");
        }
        
        // Delete elements sample is 20, 30, 40
        System.out.println("\nDeleting Operation");
        t.delete(20);
        System.out.print("After Deleting 20: ");
        t.InorderPrint();
        
        //For value 30
        t.delete(30);
        System.out.print("After Deleting 30: ");
        t.InorderPrint();

        //for value 40
        t.delete(50);
        System.out.print("After Deleting 50: ");
        t.InorderPrint();

        scan.close();
    }
}
}