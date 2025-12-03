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

    public static void main(String[] args) { 
        List<String> lines = read("c:\\dev\\data\\aoc\\2025_day3t.txt");
        int ans = 0, ans2 = 0;

        for (String line : lines) {
        }

        out.println("part I correct?  " + (ans == 15632)); // 15 for t.txt (test input)
        out.println("part II correct? " + (ans2 == 14416)); // 11 for test input
        out.println("\tsize: " + lines.size() + " part I: " + ans + " part II: " + ans2 + "\n");
    }
}
