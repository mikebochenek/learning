import java.nio.file.*;
import java.util.List;
import static java.lang.System.out;
import java.util.Arrays;

public class aoc2022_2 { // just keep hacking, and testing the borders

    public static List<String> read(String fn) {
        try {
            List<String> lines = Files.readAllLines(Paths.get(fn)); 
            return lines;
        } catch (java.io.IOException ioe) {
            out.println(ioe);
        }
        return null;
    }

    public static void main(String[] args) { //} testFromWikipedia() {
        List<String> lines = read("c:\\dev\\data\\aoc\\2022_day1.txt");
        int ans = 0, ans2 = 0;

        int elfs[] = new int[lines.size() / 2] ;
        int elfidx = 0;
        for (String line : lines) {
            if ("".equals(line)) {
                elfidx++; // blank line, is a new elf 
            } else {
                int y = Integer.parseInt(line);    
                elfs[elfidx] += y;
            }
        }

        Arrays.sort(elfs);
        ans2 = (elfs[elfs.length - 1] + elfs[elfs.length - 2] + elfs[elfs.length - 3]);
        ans = (elfs[elfs.length - 1]);

        out.println("part I correct?  " + (ans == 66616));
        out.println("part II correct? " + (ans2 == 199172));
        out.println("\t" + lines.size() + " part I: " + ans + " part II: " + ans2);
    }
}
