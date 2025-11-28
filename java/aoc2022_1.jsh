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
        elfidx++;
    } else {
        int y = Integer.parseInt(line);    
        elfs[elfidx] += y;
    }
}

for (int elf : elfs) {
    if (elf != 0) {
        //out.println(elf);
        if (ans < elf) {
            ans = elf; // new maximum
        }
    }
}

out.println("part I correct? " + (ans == 66616));
out.println("\t" + lines.size() + " part I: " + ans + " part II: " + ans2);

/exit
