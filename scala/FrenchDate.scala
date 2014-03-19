package zoo

import java.util.{Date, Locale}
import java.text.DateFormat
import java.text.DateFormat._ // uses the underscore character (_) instead of the asterisk (*)

object FrenchDate {
  def main(args: Array[String]) {
    val now = new Date
    val df = getDateInstance(LONG, Locale.FRENCH)
    println (df format now) // infix syntax, same as "df.format(now)"
  }
}