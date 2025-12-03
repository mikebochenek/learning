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

    public static long max(String input, int depth) {
        char[] charArray = input.toCharArray();
        charArray[charArray.length - 1] = '0'; // only needed for left digit
        Arrays.sort(charArray);
        String reverse = new StringBuffer(new String(charArray)).reverse().toString();
        char maxDigit = reverse.charAt(0);

        String ans = ""+maxDigit;
        for (int i = 1; i < depth; i++) {
            int idx = input.indexOf(maxDigit);
            input = input.substring(idx+1);
            //out.println(idx + " --> new input " + input);
            charArray = input.toCharArray();

            Arrays.sort(charArray);
            reverse = new StringBuffer(new String(charArray)).reverse().toString();
            //System.out.println(input + " --> " + maxDigit +  reverse.charAt(0));  
            int minDigit = reverse.charAt(0);

            //out.println("ans:" + ans + " mindigit " + Character.getNumericValue(minDigit));
            ans += (""+Character.getNumericValue(minDigit));
        }

        return Long.parseLong(ans); 
        //Character.getNumericValue(maxDigit) * 10 + Character.getNumericValue(minDigit);
    }

    public static long calc(String fn, int d) {
        List<String> lines = read("c:\\dev\\data\\aoc\\" + fn);
        long ans = 0;

        for (String line : lines) {
            long a = max(line, d);
            //out.println(line + " -> " + a);
            ans += a;
        }
        
        out.println("\tsize: " + lines.size() + " ans: " + ans + "\n");

        return ans;
    }

    public static void main(String[] args) { 
        out.println("------");        
        out.println("part I correct?  " + (calc("2025_day3t.txt", 2) == 357)); 
        //out.println("part I answer  "   + (calc("2025_day3.txt", 2) == 16842)); 

        out.println("part II correct? " + (calc("2025_day3t.txt", 12) == 3121910778619l)); 

        //out.println("part II correct? " + (ans2 == 14416)); 
    }
}
