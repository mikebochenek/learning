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
            ans += score;            

            score = 0;
            // part II: X need to lose, Y need a draw, and Z means need to win.
            if ("A".equals(p[0])) { // rock
                if ("X".equals(p[1])) score += 0 + 3; // need to lose, pick scissors
                if ("Y".equals(p[1])) score += 3 + 1; // need to tie, pick rock
                if ("Z".equals(p[1])) score += 6 + 2; // need to win, pick paper
            } else if ("B".equals(p[0])) { // paper 
                if ("X".equals(p[1])) score += 0 + 1; // need to lose, pick rock
                if ("Y".equals(p[1])) score += 3 + 2; // need to tie, pick paper
                if ("Z".equals(p[1])) score += 6 + 3; // need to win, pick scissors
            } else if ("C".equals(p[0])) { // scissors 
                if ("X".equals(p[1])) score += 0 + 2; // need to lose, pick paper
                if ("Y".equals(p[1])) score += 3 + 3; // need to tie, pick scissors
                if ("Z".equals(p[1])) score += 6 + 1; // need to win, pick rock
            } // can't believe I cut and pasted those 3 IF statements above

            ans2 += score;
            //out.println(line + " -> " + score);
        }

        out.println("part I correct?  " + (ans == 15632)); // 15 for t.txt (test input)
        out.println("part II correct? " + (ans2 == 14416)); // 11 for test input
        out.println("\tsize: " + lines.size() + " part I: " + ans + " part II: " + ans2 + "\n");
    }
}
