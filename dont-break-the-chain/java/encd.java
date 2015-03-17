package xxx;


import java.nio.charset.Charset;
import java.util.SortedMap;

public class encd {

	public static void main(String[] args) {
		String input = "27.02.2015   CREDIT SUISSE AG";
		
		SortedMap<String, Charset> map = Charset.availableCharsets();
		for (Charset testcharacterset : map.values()) {
			
			String output = new String(input.getBytes(), testcharacterset);
			
			if (!output.startsWith("27")) {
				
				if (output.contains("K")) {
					System.out.println(testcharacterset.toString() + "  " + output);			
				}
				
				System.out.println(testcharacterset.toString() + "  " + output);			
			}
		}
	}
}
