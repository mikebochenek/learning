package zoo

class Printer(val greeting: String) {
  def printMessage(): Unit = println(greeting + "!")
  def printNumber(x: Int): Unit = {
    println("Number: " + x)
  }
}

object Printer {

  val twice: Int => Int = _ * 2

  def runTwice(body: => Unit) = {
    body
    body
  }

  def main(args: Array[String]): Unit = {
    val printy = new Printer("Hi")
    printy.printMessage()
    printy.printNumber(5)

    runTwice { // this will print Hello twice
      println("Hello")
    }

    println(successors.get(5))
    println(successors.get(3))
    println(messages)

  }

  val messages: Seq[String] = Seq("Hello", "World.", "!")

  val successors = Map(1 -> 2, 2 -> 3, 3 -> 4)
  successors.get(5) match {
    case Some(n) => println(s"Successor is: $n")
    case None => println("Could not find successor.")
  }

  class Position(val x: Int, val y: Int) {
    def +(that: Position) = new Position(x + that.x, y + that.y)
  }
}

object Test {
  val Pi = 3.14
}

trait Logging {
  def log(s: String): Unit
  def warn(s: String) = log("WARN: " + s)
  def error(s: String) = log("ERROR: " + s)
}
class PrintLogging extends Logging {
  def log(s: String) = println(s)
}

class Pair[P, Q](val first: P, val second: Q)

// val twice: Int => Int = (x: Int) => x * 2

