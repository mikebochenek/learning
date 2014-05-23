package test1

/**
 *  Apart from inheriting code from a super-class, a Scala class can also import code
 * from one or several traits.
 *
 * Maybe the easiest way for a Java programmer to understand what traitss are is to
 * view them as interfaces which can also contain code. In Scala, when a class inherits
 * from a trait, it implements that traits’s interface, and inherits all the code contained
 * in the trait.
 */
object Traits {
  def main(args: Array[String]): Unit = {}
}

trait Ord {
  def <(that: Any): Boolean
  def <=(that: Any): Boolean = (this < that) || (this == that)
  def >(that: Any): Boolean = !(this <= that)
  def >=(that: Any): Boolean = !(this < that)
}

class Date(y: Int, m: Int, d: Int) extends Ord {
  def year = y
  def month = m
  def day = d
  override def toString(): String = year + "" + month + "" + day

  def <(that: Any): Boolean = {
    if (!that.isInstanceOf[Date])
      error("cannot compare " + that + " and a Date")
    val o = that.asInstanceOf[Date]
    (year < o.year) ||
      (year == o.year && (month < o.month ||
        (month == o.month && day < o.day)))
  }

  override def equals(that: Any): Boolean =
    that.isInstanceOf[Date] && {
      val o = that.asInstanceOf[Date]
      o.day == day && o.month == month && o.year == year
    }
}