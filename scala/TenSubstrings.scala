package zoo

/**
 * My solution for problem defined at: https://projecteuler.net/problem=529
 *
 * A 10-substring of a number is a substring of its digits that sum to 10.
 * For example, the 10-substrings of the number 3523014 are:
 *
 * 3523014
 * 3523014
 * 3523014
 * 3523014
 *
 * A number is called 10-substring-friendly if every one of its digits belongs to a 10-substring.
 * For example, 3523014 is 10-substring-friendly, but 28546 is not.
 *
 * Let T(n) be the number of 10-substring-friendly numbers from 1 to 10n (inclusive).
 * For example T(2) = 9 and T(5) = 3492.
 *
 * Find T(1018) mod 1 000 000 007.
 */
object TenSubstrings {

  def main(args: Array[String]): Unit = {
    basicTest()
    println("bruteforce 100 is: " + bruteForce(2.0))
    println("bruteforce 10'000 is: " + bruteForce(5.0))
  }
  
  def bruteForce(i: Double): Int = {
    val max = Math.pow(10, i).toInt
    var count = 0;
    
    for (i <- 0 to max) {
      if (isTenSubstring(""+i) && isTenSubstring((""+i).reverse)) {
        count += 1
      }
    }  
    
    count
  }
  
  def basicTest() {
    for (test <- Array("3523014", "28546")) {
      println(test + " belongs to a 10-substring? " + isTenSubstring(test))
    }
  }

  def isTenSubstring(str: String): Boolean = {
    val array = new Array[Integer](str.length())
    for (i <- 0 until str.length()) {
      val parsedInt = Integer.parseInt("" + str.charAt(i))
      array(i) = parsedInt;
    }

    for (i <- 0 until array.length) {
      //println ("---- " + i)
      var counter = 0;
      var idx = i;
      while (counter != 10 && idx < array.length) {
        counter += array(idx)
        //println (counter + " + " + array(idx))
        idx += 1
        if (counter > 10 /*|| (idx == array.length && counter != 10)*/) {
          return false
        }
      }

    }

    true
  }
}
