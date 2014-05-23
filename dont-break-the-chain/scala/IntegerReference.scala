package test1

object IntegerReference {

  def main(args: Array[String]): Unit = {
    val cell = new Reference[Int]
    cell.set(13)
    println("Reference contains the half of " + (cell.get * 2))
  }
}

/** 
 *  The class Reference is parametrized by a type, called T, which is the type of its element.
 * This type is used in the body of the class as the type of the contents variable,
 * the argument of the set method, and the return type of the get method.
 */
class Reference[T] {
  private var contents: T = _
  def set(value: T) { contents = value }
  def get: T = contents
}