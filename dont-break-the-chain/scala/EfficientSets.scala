package test1

import scala.util.Random

/**
 * coding-kata-comparing-2-sets-efficiently
 *
 * Given the two sets of integers S1 and S2 and the methods M1, M2 and M3,
 * write a program/algorithm which compares the values between the two sets so that:
 *
 * For every integer present in S1 and not in S2 you call M1;
 * For every integer present in S2 and not in S1 you call M2;
 * For every integer present in both S1 and S2 you call M3.
 *
 * Note:
 * We don't care about what M1, M2 and M3 does;
 * The two sets can be of different sizes;
 * The two sets can be extremely large;
 * The sets may or may not be sorted.
 */
object EfficientSets {
  def compare(a: List[Int], b: List[Int]) = {
    val aSorted = collection.SortedSet(a.sortWith(_ < _): _*)
    val bSorted = collection.SortedSet(b.sortWith(_ < _): _*)
    /* http://stackoverflow.com/questions/6674156/convert-list-of-ints-to-a-sortedset-in-scala */

    for (x <- aSorted) {
      if (bSorted.contains(x)) m3(x)
      else m1(x)
    }

    for (x <- bSorted) {
      if (aSorted.contains(x)) Nil // i.e. do nothing
      else m2(x)
    }
  }

  def m1(x: Int) = apply("M1(" + x + ");")
  def m2(x: Int) = apply("M2(" + x + ");")
  def m3(x: Int) = apply("M3(" + x + ");")
  def apply(str: String) = Nil; //println (str)
  
  def main(args: Array[String]) = {
    compare(List(1, 2, 3, 5), List(1, 3, 6))
    timeTest(1000000)
  }

  /* http://stackoverflow.com/questions/9094820/generating-a-list-of-random-numbers */
  def generateRandomArray(size: Int) = List.fill(size)(Random.nextInt)

  def timeTest(size: Int) = {
    val rand1 = generateRandomArray(size)
    val rand2 = generateRandomArray(size)

    val start = System.currentTimeMillis();
    compare(rand1, rand2)
    println((System.currentTimeMillis() - start) + "ms expired with size=" + size)
  }
}
