package topcoder

import org.junit.Test
import org.junit.Assert._

/**
 * Josh loves playing with blocks. Currently, he has N blocks, labeled 0 through N-1.
 * The heights of all blocks are positive integers. More precisely, for each i, the
 * height of block i is blockHeights[i]. Josh is interested in making the tallest
 * block tower possible. He likes all his towers to follow three simple rules:
 *
 * The blocks must be stacked in a single column, one atop another. The height of
 * the tower is simply the sum of heights of all its blocks.
 *
 * The labels of blocks used in the tower must increase from the bottom to the top.
 * In other words, whenever Josh places box x on top of box y, we have x > y.
 *
 * Josh will never place a box of an even height on top of a box of an odd height.
 *
 * You are given the int[] blockHeights. Return the height of the tallest
 * possible block tower Josh can build.
 *
 * Constraints
 * -	blockHeights will contain between 1 and 50 elements, inclusive.
 * -	Each element of blockHeights will be between 1 and 50, inclusive.
 */
class BlockTower {

  def getTallest(blockHeights: Array[Int]): Int = {
    var h = 0
    var previousOddHeight = false
    for (i : Int <- blockHeights) {
      if (!previousOddHeight) {
        h += i
      }
      previousOddHeight = i % 2 == 1
    }
    h
  }

  @Test def test0() { assertEquals(11, getTallest(Array(4, 7))) }
  @Test def test1() { assertEquals(7, getTallest(Array(7, 4))) }
  @Test def test2() { assertEquals(7, getTallest(Array(7))) }
  @Test def test3() { assertEquals(4, getTallest(Array(4))) }
  @Test def test4() { assertEquals(196, getTallest(Array(48, 1, 50, 1, 50, 1, 48))) }
  @Test def test5() { assertEquals(147, getTallest(Array(49, 2, 49, 2, 49))) }
  @Test def test6() { assertEquals(273, getTallest(Array(44, 3, 44, 3, 44, 47, 2, 47, 2, 47, 2))) }

}