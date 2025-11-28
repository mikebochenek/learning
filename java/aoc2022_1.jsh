import java.nio.file.*;
import java.util.List;
import static java.lang.System.out;

List<String> lines = Files.readAllLines(Paths.get("c:\\dev\\data\\aoc\\2022_day1.txt")); 
 
int ans = 0, ans2 = 0;
for (String line : lines) {
}

out.println(java.time.LocalTime.now().toString() + " " + lines.size() 
    + " part I: " + ans);

/exit
