import java.nio.file.*;
import java.util.List;
import static java.lang.System.out;
import java.util.Arrays;

public class aoc2025_3 { 

    public static List<String> read(String fn) {
        try {
            return Files.readAllLines(Paths.get(fn)); 
        } catch (java.io.IOException ioe) {
            out.println(ioe);
            return null;
        }
    }

    public static int max(String input) {
        char[] charArray = input.toCharArray();
        charArray[charArray.length - 1] = '0'; // only needed for left digit
        Arrays.sort(charArray);
        String reverse = new StringBuffer(new String(charArray)).reverse().toString();
        char maxDigit = reverse.charAt(0);

        int idx = input.indexOf(maxDigit);
        //out.println(idx);
        input = input.substring(idx+1);
        //out.println(" --> new input " + input);
        charArray = input.toCharArray();
        Arrays.sort(charArray);
        reverse = new StringBuffer(new String(charArray)).reverse().toString();
        //System.out.println(input + " --> " + maxDigit +  reverse.charAt(0));  
        int minDigit = reverse.charAt(0);

        return Character.getNumericValue(maxDigit) * 10 + Character.getNumericValue(minDigit);
    }

    public static int calc(String fn) {
        List<String> lines = read("c:\\dev\\data\\aoc\\" + fn);
        int ans = 0;

        for (String line : lines) {
            //out.println("->" + line);
            ans += max(line);
        }
        
        out.println("\tsize: " + lines.size() + " ans: " + ans + "\n");

        return ans;
    }

    public static void main(String[] args) { 
        
        out.println("part I correct?  " + (calc("2025_day3t.txt") == 357)); 
        out.println("part I answer  " + (calc("2025_day3.txt") == 16842)); 

        //out.println("part II correct? " + (ans2 == 14416)); 
    }
}
