package zoo

object Timer {
  def main(args: Array[String]) {
    println("here we go...")
    val c = new Complex(2.3, 1.9)
    oncePerSecond(() => println("keep looping forever"))
    
  }
  
  def oncePerSecond(callback: () => Unit) {
    while (true) {
      callback()
      Thread sleep 1000
    }
  }

}