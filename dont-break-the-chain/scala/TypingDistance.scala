package topcoder

import org.junit.Test
import org.junit.Assert._

/**
 * Problem Statement
 * Jakub is trying out a one-dimensional keyboard. It consists of a single row of keys. 
 * The distance between any two adjacent keys is 1. Each key contains a distinct letter 
 * of the English alphabet. Jakub uses only one finger to type on the keyboard. 
 * He wonders what is the smallest total distance he will have to move his finger 
 * while typing a given word.
 *
 * For example, if the keyboard's only row is "qwertyuiop", and Jakub wants to type 
 * the word "potter", he will have to move his finger from 'p' to 'o' (distance 1), 
 * from 'o' to 't' (distance 4), from 't' to 't' (distance 0), from 't' to 'e' 
 * (distance 2) and from 'e' to 'r' (distance 1), for a total distance 
 * of 1 + 4 + 0 + 2 + 1 = 8.
 *
 * You are given a String keyboard and a String word, describing the keyboard and 
 * the word Jakub wants to write. Return the minimum distance he will have to move 
 * his finger in order to type the word on the keyboard.
 */
class TypingDistance {

  // probably best solved (tail) recursively, since we are functional programming experts :-)
  def minDistance(keyboard: String, word: String): Int = {
    def md(current: Char, subword: String): Int = {
      if (subword.length() == 0) 0
      else Math.abs(keyboard.indexOf(current) - keyboard.indexOf(subword.charAt(0))) + md(subword.charAt(0), subword.substring(1))
    } // hmmm what if indexOf doesn't find it?
    md(word.charAt(0), word.substring(1));
  }
  
  @Test def test0() { assertEquals(8, minDistance("qwertyuiop", "potter"))}
  @Test def test1() { assertEquals(9, minDistance("tc", "tctcttccctccccttc"))}
  @Test def test2() { assertEquals(0, minDistance("a", "aaaaaaaaaaa"))}
  @Test def test3() { assertEquals(39, minDistance("kwadrutove", "rowerowe"))}
  @Test def test4() { assertEquals(322, minDistance("qwertyuiopasdfghjklzxcvbnm", "topcodersingleroundmatchgoodluckhavefun"))}
}