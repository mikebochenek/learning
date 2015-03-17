package zoo

/**
 * The following exercises are designed to test your knowledge of the Scala programming language. They cover the content presented in this chapter, along with some additional Scala features. The last two exercises contrast the difference between concurrent and distributed programming, as defined in this chapter. You should solve them by sketching out a pseudocode solution, rather than a complete Scala program.
 *
 */
object Chapter1Exercises {

  def main(args: Array[String]): Unit = {
    compose(null, null, null)
    
  }

  /**
   * Implement a compose method with the following signature:
   * def compose[A, B, C](g: B => C, f: A => B): A => C = ???
   * This method must return a function h, which is the composition of the functions f and g.
   *
   */
  def compose(a: => Unit, b: => Unit, c: => Unit) {
    

  }

  /**
   * Implement a fuse method with the following signature:
   * def fuse[A, B](a: Option[A], b: Option[B]): Option[(A, B)] = ???
   * The resulting Option object should contain a tuple of values from the Option objects a and b, given that both a and b are non-empty. Use for-comprehensions.
   *
   */
  def fuse() {

  }

  /**
   * Implement a check method, which takes a set of values of the type T and a function of the type T => Boolean:
   * def check[T](xs: Seq[T])(pred: T => Boolean): Boolean = ???
   * The method must return true if and only if the pred function returns true for all the values in xs without throwing an exception. Use the check method as follows:
   *
   * check(0 until 10)(40 / _ > 0)
   *
   * Tip
   * The check method has a curried definition: instead of just one parameter list, it has two of them. Curried definitions allow a nicer syntax when calling the function, but are otherwise semantically equivalent to single-parameter list definitions.
   */
  def check() {

  }
}