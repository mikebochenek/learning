package zoo

/**
 * coding-kata-efficiently-generating-lottery-numbers
 * http://stackoverflow.com/questions/9094820/generating-a-list-of-random-numbers
 * 
 * Generating Lottery Numbers
 *
 * Inspired by my desperate need to win the EuroMillions (currently £128,000,000)
 *
 * Write a method that takes 2 integers, a = amount of numbers,
 * b = range of numbers (between 0 and b) and produces a list of numbers
 * for me to play in the lottery. i.e. the equivilant of a lucky dip.
 *
 * example:
 *
 * public int[] LuckyDip(int lineSize, int range) { ... }
 *
 * // produce 6 numbers between 0 and 50
 * int[] myNumbers = LuckyDip(6, 50);
 * // produce 2 numbers between 0 and 10
 * int[] myNumbers = LuckyDip(2, 10);
 * Efficiently
 *
 * We are looking for efficiency because I want to generate many lines to buy,
 * so please provide time and space metrics in Big-O notation with your answer.
 * In addition to the voting below, please only vote up answers that
 * are efficient rather than just elegant.
 *
 */
object EfficientlyGeneratingLotteryNumbers {
  def luckyDip(lineSize: Integer, range: Integer) = {
    util.Random.shuffle((0 to range).toList).take(lineSize)
  }
  
  def main(args: Array[String]): Unit = {
    println(luckyDip(6, 50))
    println(luckyDip(2, 10))
  }
}
