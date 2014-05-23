package test1

import org.junit.Test
import org.junit.Assert._

class HelloJUnit {

  @Test def x(){
    val c = new Complex(1.2, 3)
    assertTrue(3 == c.im)
  }
}

/**
 * Methods without arguments: doable in Scala, simply by defining them as methods without
 * arguments. Such methods differ from methods with zero arguments in that they don’t 
 * have parenthesis after their name, neither in their definition nor in their use.
 */
class Complex(real: Double, imaginary: Double) { // scala.AnyRef is implicitly extended
  def re = real
  def im = imaginary
  
  // It is mandatory to explicitly specify that a method overrides another one using the
  // override modifier, in order to avoid accidental overriding.
  override def toString() = "" + re + (if (im < 0) "" else "+") + im + "i"
}