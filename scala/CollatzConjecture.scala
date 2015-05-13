package zoo

/**
 * http://blogs.ams.org/matheducation/2015/05/01/famous-unsolved-math-problems-as-homework/
 *
 * Given a positive integer n, if it is odd then calculate 3n+1.  If it is even, calculate n/2.
 * Repeat this process with the resulting value. For example, if you begin with 1, then you obtain
 * the sequence 1,4,2,1,4,2,1,4,2,1,...  which will repeat forever in this way.  If you start
 * with a 5, then you obtain the sequence 5,16,8,4,2,1,..., and now find yourself in the previous case.
 *
 * The unsolved question about this process is: If you start from any positive integer,
 * does this process always end by cycling through 1,4,2,1,4,2,1,...?
 * Mathematicians believe that the answer is yes, though no one knows how to prove it.
 * This conjecture is known as the Collatz Conjecture (among many other names),
 * since it was first asked in 1937 by Lothar Collatz.
 */
object CollatzConjecture {

  var count = 0;
  def main(args: Array[String]): Unit = {
    val startTS = System.currentTimeMillis();
    val end = 100000
    for (i <- 1 to end) {
      // print("starting CollatzConjecture with: " + i + " --> ")
      count = 0;
      // calc(i) // this one prints the actual values
      countCalc(i) // this one only counts the number of iterations
      countCalcNonRecursively(i) // only counts as well, but using a for-loop (instead of recursion)
      // print(" finishes in " + count + " iterations\n")
    }
    println (" completed all " + end + " in " + (System.currentTimeMillis() - startTS) + " milliseconds!")
  }

  def calc(n: Integer): Unit = {
    print(n + ", ")

    if (n == 1) {
      print("4, 2, 1, ... \n")
    } else if (n % 2 == 0) {
      calc(n / 2)
    } else {
      calc(3 * n + 1)
    }
  }
  
  def countCalc(n: Integer): Unit = {
    count = count + 1;

    if (n == 1) {
      return
    } else if (n % 2 == 0) {
      countCalc(n / 2)
    } else {
      countCalc(3 * n + 1)
    }
  }
  
  def countCalcNonRecursively(input: Integer): Integer = {
    var n = input;
    var counter = 0;
    while (n != 1) {
      counter = counter + 1
      if (n % 2 == 0) {
        n = n / 2
      } else {
        n = 3 * n + 1
      }
    }
    return counter;
  }

}