package zoo

/**
 * Output :	number of inversions = number of pairs (i,j) of
 * array indices with i<j and A[i] > A[j] 
 */
object Inversions {

  def main(args: Array[String]): Unit = {
    val startTS = System.currentTimeMillis();

    // http://bcomposes.wordpress.com/2011/09/19/first-steps-in-scala-for-beginning-programmers-part-8/
    // http://stackoverflow.com/questions/1284423/read-entire-file-in-scala
    val lines = scala.io.Source.fromFile("/home/mike/Downloads/IntegerArray.txt", "utf-8").mkString.split("\\n")

    var count : Long = 0

    //http://stackoverflow.com/questions/6833501/efficient-iteration-with-index-in-scala
    //for (i <- 0 to lines.length-1) println("String # " + i + " is "+ lines(i))

    for (i <- 0 to lines.length - 1) {
      for (j <- (i+1) to lines.length - 1) {
        if (lines(i) < lines(j)) {
          count = count + 1
        }
      }
    }

    println("count is " + count)
    println(lines.length + " lines read in " + (System.currentTimeMillis() - startTS) + "ms")
  }

}