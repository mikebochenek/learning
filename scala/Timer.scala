package zoo

/**
 * 4.2 Functions are objects
 * Perhaps more surprising for the Java programmer, functions are also objects in Scala.
 * It is therefore possible to pass functions as arguments, to store them in variables,
 * and to return them from other functions. This ability to manipulate functions as
 * values is one of the cornerstone of a very interesting programming paradigm called
 * functional programming.
 */
object Timer {
  def main(args: Array[String]) {
    println("here we go...")
    val c = new Complex(2.3, 1.9)
    val o = (1).+(((2).*(3))./(4)) // same as 1 + 2 * 3 / 4
    oncePerSecond(() => println("keep looping forever")) // Anonymous Functions
  }
  
  def oncePerSecond(callback: () => Unit) {
    while (true) {
      callback()
      Thread sleep 1000
    }
  }

}