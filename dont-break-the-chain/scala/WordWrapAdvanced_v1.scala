package zoo

/**
 * coding-kata-word-wrap-advanced
 */
object WordWrapAdvanced {

  val test1 = "1. Life isn’t about getting and having, it’s about giving and being. –Kevin Kruse"
  val test2 = "I attribute my success to this: I never gave or took any excuse. –Florence Nightingale"
  val test3 = "You miss 100% of the shots you don’t take. –Wayne Gretzky"
  val test4 = "I’ve missed more than 9000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life. And that is why I succeed. –Michael Jordan"
  
  def main(args: Array[String]): Unit = {
    println(wrap(test1, 20, "m") + "\n")
    println(wrap(test2, 20, "m") + "\n")
    println(wrap(test3, 30, "m") + "\n")
    println(wrap(test4, 40, "m") + "\n")
  }
  
  def wrap(input: String, w: Int, mode: String): String = {
    val tokens = input.split(" ")

    def wrapRec(x: String): String = {
      x
    }
    
    val modes = ("left", "right", "center", "full")
    
    var t = ""
    var total = 0
    for (x <- tokens) {
      if (x.length() + total < w) {
        t += x + " "
        total += x.length() + 1
      } else {
        t += "\n" + x + " "
        total = x.length() + 1; 
      }
     
    }
    
    t
  }

}
