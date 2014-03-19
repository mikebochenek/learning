package zoo

/**
 * One important difference is that classes in Scala can have parameters. This
 * is illustrated in the following definition of complex numbers.
 */
class Complex(real: Double, imaginary: Double) {
  def re() = real
  def im() = imaginary
  /* It should be noted that the return type of these two methods is not given explicitly.
   * It will be inferred automatically by the compiler, which looks at the right-hand side
   * of these methods and deduces that both return a value of type Double.
   * The compiler is not always able to infer types like it does here, and there is 
   * unfortunately no simple rule to know exactly when it will be, and when not. In practice, this
   * is usually not a problem since the compiler complains when it is not able to infer a
   * type which was not given explicitly. 
   */

  /**
   * but this is not what I really want though
   */
  def + (other: Complex) {
    this.im + other.im;
  }
}