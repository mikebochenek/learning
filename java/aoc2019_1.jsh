import java.nio.file.*;
import java.util.List;
// import static System.out.println;

/* https://claude.ai/chat/26f09566-c2b9-495e-b116-c4487d98cde9
 * whats the simplest or shortest java code snippet to read multiple lines from an input file?
 * claude is about simplifying the search: getting lucky at interpreting what I am looking for
 */
List<String> lines = Files.readAllLines(Paths.get("c:\\dev\\data\\aoc\\2019_day1.txt"));
// for (String line : lines) {
//     System.out.println(line);
// }

System.out.println("aoc -> " + lines.size());

/exit
