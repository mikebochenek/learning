import java.nio.file.*;
import java.util.List;
import static java.lang.System.out;
import java.util.Arrays;

public class aoc2022_2 { // just keep hacking, and testing the borders

    public static List<String> read(String fn) {
        try {
            return Files.readAllLines(Paths.get(fn)); 
        } catch (java.io.IOException ioe) {
            out.println(ioe);
            return null;
        }
    }

    public static void main(String[] args) { 
        List<String> lines = read("c:\\dev\\data\\aoc\\2022_day2.txt");
        int ans = 0, ans2 = 0;

        // A for Rock, B for Paper, and C for Scissors
        // X for Rock, Y for Paper, and Z for Scissors
        for (String line : lines) {
            String[] p = line.split(" ");
            // do loss first & I wonder if there is a shortcut (1,2,3 - minus)

            int score = 1;
            score += ("Y".equals(p[1])) ? 1 : 0;
            score += ("Z".equals(p[1])) ? 2 : 0;

            if (("A".equals(p[0]) && "Z".equals(p[1])  // scissors loses against rock
                || ("B".equals(p[0]) && "X".equals(p[1]))) // rock loses against paper
                || ("C".equals(p[0]) && "Y".equals(p[1]))) { // paper loses against scissors
                score += 0;
            } else if (("A".equals(p[0]) && "Y".equals(p[1])) // paper beats rock
                || ("B".equals(p[0]) && "Z".equals(p[1])) // scissors beats paper
                || ("C".equals(p[0]) && "X".equals(p[1]))) { // rock beats scissors
                score += 6; // win
            } else {
                score += 3; // tie 
            }
            //out.println(line + " -> " + score);

            ans += score;            
        }

        out.println("part I correct?  " + (ans == 15632)); // 15 for t.txt (test input)
        out.println("part II correct? " + (ans2 == 199172));
        out.println("\tsize: " + lines.size() + " part I: " + ans + " part II: " + ans2 + "\n");
    }
}
