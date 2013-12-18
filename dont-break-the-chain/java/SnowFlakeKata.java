public class SnowFlakeKata {
	public static void main(String[] args) {
		SnowFlakeKata snowflake = new SnowFlakeKata();
		snowflake.gen(1);
		snowflake.gen(3);
		snowflake.gen(5);
	}
	void gen(int r) { // vertical symmetry created by two for loops
		for (int i = 0; i < r*2; i++) { draw(getString(i)); }
		for (int i = 0; i < r*2; i++) { draw(getString(r*2-i)); }
	}
	void draw(String s) { System.out.printf("%25s%s\n", s, reverse(s)); }
	// horizontal symmetry created by printing s and reverse(s)

	String getString(int r) {
		final String[] x = {"/", "\\", "|", "+"}; //TODO rearrange or add more elements to generate your own designs!
		String s = "";
		for (int i = 0; i < r; i++) {
			s += x[i % x.length] + " ";
		}
		return s;
	}
	String reverse(String s) { // even wrote my very own reverse function!
		if (s.length() <= 1) return s;
		else return s.charAt(s.length() - 1) + (s.length() > 1 ? reverse(s.substring(0, s.length()-1)) : ""); 
	}
}
