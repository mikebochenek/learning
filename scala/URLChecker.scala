package zoo

import scala.io.Source
import sys.process._
import java.net.URL
import java.io.File
											
/**
 * http://alvinalexander.com/scala/scala-how-to-download-url-contents-to-string-file
 */
object URLChecker {

  def main(args: Array[String]): Unit = {
    val html = Source.fromURL("http://www.bochenek.ca").mkString
    println(html.contains("I'm Mike Bochenek"))
    
    new URL("http://www.bochenek.ca") #> new File("/tmp/Output.html") !!
  }

}