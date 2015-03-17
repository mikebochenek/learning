package zoo

/**
 * A new lottery starts and follows some basic rules:
 *
 * $1 per ticket
 * For each ticket 4 numbers are chosen at random
 * Each number on the ticket is whole number from 1 to 100
 * 4 whole numbers from 1 to 100 are drawn at random on a weekly basis
 * Prizes are then given for each ticket based on how many matching numbers were on that ticket:
 *
 * 0 out of 4 numbers = $0
 * 1 out of 4 numbers = $1
 * 2 out of 4 numbers = $100
 * 3 out of 4 numbers = $1,000
 * 4 out of 4 numbers = $10,000,000
 * Write code that allows a potential player of this lottery to simulate their net loss / gain
 * by specifying how many tickets they would like to play each week and how many weeks they would like to play for.
 *
 * E.g. If they specified 3 tickets a week for 2 weeks. And on the first week 1 ticket
 * matched 1 number and all 5 other tickets matched 0 numbers then they would have a net of -$5.
 *
 * Give some examples of how much you "made" after a few years of playing.
 */
object LotterySimulator {
  def main(args: Array[String]): Unit = {
    println("10 tickets per week for 52 weeks yields: " + simulate(10, 52))
    println("1000 tickets per week for 52 weeks yields: " + simulate(1000, 52))
    println("10000 tickets per week for 5 weeks yields: " + simulate(10000, 5))
  }

  def draw(): List[Int] = util.Random.shuffle((1 to 100).toList).take(4)

  def simulate(tickets: Int, weeks: Int): Int = {
    simulateweek(tickets, draw) + (if (weeks > 0) simulate(tickets, weeks - 1) else 0)
  }

  def simulateweek(tickets: Int, winning: List[Int]): Int = {
    def prize(test: List[Int]): Int = {
      var matchingNumbers = 0;
      winning.foreach((w: Int) => if (test.contains(w)) matchingNumbers += 1)
      matchingNumbers match {
        case 4 => 10000000
        case 3 => 1000
        case 2 => 100
        case 1 => 1
        case 0 => 0
      }
    }
    prize(draw) - 1 + (if (tickets > 0) simulateweek(tickets - 1, winning) else 0)
  }
}


/** 
    // http://stackoverflow.com/questions/20058366/shuffle-a-list-of-integers-with-java-8-streams-api
    //println("matches " + matches  + "  " + winning +  "    " + test)

    // winning.zip(test)
    //for (w <- winning) if test.contains(w) { matches += 1 }
    // if (test.contains(winning(0))) { matches += 1 } 
    // http://stackoverflow.com/questions/17812486/comparing-items-in-two-lists
    // val m = winning.zip(test).filter(x => x._1==x._2).size
*/
