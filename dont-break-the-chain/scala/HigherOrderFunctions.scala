package zoo

/** 
 * http://en.wikibooks.org/wiki/Scala/Higher-order_functions_1
 * [what a great resource - wikibooks! 
 */
object HigherOrderFunctions {

  def main(args: Array[String]): Unit = {
    def isEqualToFour(a: Int) = a == 4
    val list = List(1, 2, 3, 4)
    val resultExists4 = list.exists(isEqualToFour)
    println(resultExists4) //Prints "true".
  }

}