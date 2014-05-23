/*
 * scalac FrenchDate.scala
 *
 * scala -classpath . FrenchDate
 */
 
import java.util.{Date, Locale}
import java.text.DateFormat
import java.text.DateFormat._

object FrenchDate {
	def main(args: Array[String]) {
		val exp = (1).+(((2).*(3))./(4)) // exactly same as 1 + 2 * 3 / 4
	
		val now = new Date
		val df = getDateInstance(LONG, Locale.FRANCE)
		println(df format now) // with an infix syntax, same as "df.format(now)"
	}
}