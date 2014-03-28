package zoo

object SpendingHXKata {

  def main(args: Array[String]): Unit = {
    val catalog = Map(5 -> "stapler", 3 -> "pen", 2 -> "pencil", 1 -> "paper")
    spend(catalog, 10)
  }
  
  def spend(c: Map[Int, String], amount: Int) {
    val basket: List[String] = List()
    c.keys.foreach(i => if (amount == i) { basket+c(i) }  )
  }

}