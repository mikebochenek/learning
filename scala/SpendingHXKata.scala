package zoo

import scala.collection.mutable.MutableList

object SpendingHXKata {

  def main(args: Array[String]): Unit = {
    val catalog = Map(5 -> "stapler", 3 -> "pen", 2 -> "pencil", 1 -> "paper")
    val basket: MutableList[String] = MutableList()

    spend(catalog, 5, basket)
  }
  
  def spend(c: Map[Int, String], amount: Int, basket: MutableList[String]) {
    
    c.keys.foreach(i => if (amount <= i && amount > 0) {
      basket += c(i)
      spend(c, amount - i, basket)
    })
    
    if (!basket.isEmpty && amount == 0) println(basket)
  }

}