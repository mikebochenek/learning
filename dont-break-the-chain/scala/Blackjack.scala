package zoo

/**
 * code-golf-blackjack
 *
 * Problem
 * Write a program that prints the score of the card game 21 (also known as Blackjack)
 *
 * Blackjack Scoring
 * A hand consists of one or more cards and the score is the total of the card values in the hand.
 *
 * Face cards (King, Queen, Jack) are counted as 10 points.
 * Aces are counted as either 1 or 11 points.
 * All other cards are counted as the numeric value showed on the card. The hand's score is the total value of the cards in the hand, but becomes 0 if the total exceeds 21 (bust)
 * The program must count the Ace score appropriately to maximise the total score.
 *
 * Input
 * The input is a string that represents a hand. For example "A2A3" means 4 cards, in the order of Ace, 2, Ace, 3. Ace is abbreviated as A, King as K, Queen as Q, Jack as J, and 10 as T
 *
 * It can be assumed the input is always a legal hand:
 *
 * Input does not contain unexpected characters
 * The input is upper case
 * The input is passed on the command line as a single argument
 * Input is a subset of the 52 cards (so you can't get 22222 for example)
 * A player can't get extra hands once they bust, so QQQQ is not a legal hand as they went bust at QQQ
 * Example inputs and outputs
 * +-------+--------+------------------------------------------------------------+
 * | Input | Output | Note                                                       |
 * +-------+--------+------------------------------------------------------------+
 * | 34    | 7      | Two cards 3 and 4                                          |
 * | 234   | 9      |                                                            |
 * | A234  | 20     | 11+2+3+4=20. Ace should be counted as 11 to maximise score |
 * | AJ    | 21     | 11+10=21                                                   |
 * | 2AJ   | 13     | 2+1+10=13 Can't use Ace as 11 or it would bust             |
 * | JJJ   | 0      | 10+10+10=30 which is > 21                                  |
 * | AAAA  | 14     | 11+1+1+1=14 Shows you can only use one ace                 |
 * +-------+--------+------------------------------------------------------------+
 */
object Blackjack {

    def main(args: Array[String]): Unit = {
      print("34")
      print("234")
      print("A234")
      print("AJ")
      print("2AJ") //TODO this one breaks because order of the cards is not important
      print("JJJ")
      print("AAAA")
    }
    
    def score(str: String): Int = {
      var scr = 0
      for (s <- str) {
        if (s == 'J' || s == 'Q' || s == 'K' ) scr += 10
        else if (s == 'A') {
          if (scr < 11) scr += 11
          else scr += 1
        }
        else scr += s.toInt - 48
      }
      if (scr > 21) scr = 0
      scr
    }
    
    def print(s: String) = {
      println (s +  " -> " + score(s))
    }
}
