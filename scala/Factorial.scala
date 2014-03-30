package zoo

import org.junit.Assert._
import org.junit.Test

/**
 * @author Mike Bochenek
 */
class Factorial {

  def factorial(x: Int): Int = {
    if (x <= 2) return x;
    else return x * factorial(x - 1)
  }

  @Test def test0() { assertEquals(0, factorial(0)); }
  @Test def test1() { assertEquals(1, factorial(1)); }
  @Test def test7() { assertEquals(5040, factorial(7)); }
  @Test def test10() { assertEquals(3628800, factorial(10)); }
}