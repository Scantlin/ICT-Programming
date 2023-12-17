import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Word_reversal {
   public static void main(String[] args) {
       Scanner M = new Scanner(System.in);
       print("Enter the sentence: ");
       String sentence = M.nextLine();
       System.out.println("reverse words is " + "\"" + reverse(sentence) + "\"");
       M.close();
   }

   public static String reverse(String sentence) { //a function to make the sentence reverse
        Pattern pattern = Pattern.compile("(\\b\\w+\\b)");
        Matcher matcher = pattern.matcher(sentence);
        StringBuffer reversedSentence = new StringBuffer();

        while (matcher.find()) {
            matcher.appendReplacement(reversedSentence, matcher.group(1));
        }
        matcher.appendTail(reversedSentence);

        String reversedString = reversedSentence.toString();
        Pattern pattern2 = Pattern.compile("\\s+(\\w+\\b)");
        Matcher matcher2 = pattern2.matcher(reversedString);

        StringBuffer finalReversedSentence = new StringBuffer();
        while (matcher2.find()) {
            matcher2.appendReplacement(finalReversedSentence, " " + matcher2.group(1));
        }
        matcher2.appendTail(finalReversedSentence);

        return finalReversedSentence.toString(); 
   }
   static void print(String word) {
    System.out.print(word);
   }
}