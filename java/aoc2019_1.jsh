import java.nio.file.*;
import java.util.List;
// import static System.out.println;

/* https://claude.ai/chat/26f09566-c2b9-495e-b116-c4487d98cde9
 * whats the simplest or shortest java code snippet to read multiple lines from an input file?
 * claude is about simplifying the search: getting lucky at interpreting what I am looking for
 */
List<String> lines = Files.readAllLines(Paths.get("c:\\dev\\data\\aoc\\2019_day1.txt"));

int fuel(int mass) {
    return (mass / 3) - 2;
}

int recursive_fuel(int mass) {
    f = fuel(mass);
    if (f <= 0) {
        return 0;
    } else {
        return recursive_fuel(f) + f;
    }
}

assert(false); // ?!
System.out.println((fuel(1969) == 654) + " and " + (fuel(100756) == 33583));

System.out.println("part II test:" + (recursive_fuel(14) == 2));

int total = 0;
for (String line : lines) {
    int i = Integer.parseInt(line);
    total += fuel(i);
}

System.out.println("aoc -> " + lines.size() + " part I: " + total);


/exit
