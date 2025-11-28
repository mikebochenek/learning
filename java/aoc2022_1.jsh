import java.nio.file.*;
import java.util.List;
import static java.lang.System.out;

List<String> lines = Files.readAllLines(Paths.get("c:\\dev\\data\\aoc\\2022_day1.txt")); 

int ans = 0, ans2 = 0;

// just thinking if it would be fun to do this with pandas or spark, and make it work for huge data sets
int elfs[] = new int[lines.size() / 2] 
int elfidx = 0;
for (String line : lines) {
    if ("".equals(line)) {
        elfidx++; // blank line, is a new elf 
    } else {
        int y = Integer.parseInt(line);    
        elfs[elfidx] += y;
    }
}

// first thought it to keep track of top 3, but then you realize it's faster to sort 
Arrays.sort(elfs);
ans2 = (elfs[elfs.length - 1] + elfs[elfs.length - 2] + elfs[elfs.length - 3]);
ans = (elfs[elfs.length - 1]);

/* now obsolete! 
for (int elf : elfs) {
    if (elf != 0) {
        //out.println(elf);
        if (ans < elf) {
            ans = elf; // new maximum
        }
    }
} */

out.println("part I correct?  " + (ans == 66616));
out.println("part II correct? " + (ans2 == 199172));
out.println("\t" + lines.size() + " part I: " + ans + " part II: " + ans2);

/exit
