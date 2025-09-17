public class switch_statement{
    public static void main(String[] args){
        char grade = 'B';

        switch(grade){
            case 'A':
                System.out.println(grade + ": " + "outstanding");
                break;
            case 'B':
                System.out.println("Excellence");
                break;
            case 'C':
                System.out.println("Satisfactory");
                break;
            default:
                System.out.println("Invalid Grade");
        }
    }
}