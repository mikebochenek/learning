package zoo

import scala.collection.JavaConversions._

object Solution {

  def traverse(T: Tree): Int = {
    var maxleft = 0
    var maxright = 0
    if (T.l != null) {
      log("go left at " + T)
      maxleft = 1 + traverse(T.l)
    }
    if (T.r != null) {
      log("go right at " + T)
      maxright = 1 + traverse(T.r)
    }
    log("node " + T)

    if (maxleft < maxright) maxright
    else maxleft
  }

  def solution1(T: Tree): Int = {

    def traverseleft(T: Tree): Int = {
      var maxleft = 0
      if (T.l != null) {
        log(maxleft + " go left at " + T)
        maxleft = 1 + traverseleft(T.l)
      }
      if (T.r != null) {
        log(maxleft + " go right at " + T)
        maxleft = Math.max(maxleft, traverseleft(T.r))
      }
      log(maxleft + " node " + T)
      maxleft
    }

    def traverseright(T: Tree): Int = {
      var maxright = 0
      if (T.r != null) {
        log(maxright + " go right at " + T)
        maxright = 1 + traverseright(T.r)
      }
      if (T.l != null) { // somehow, I feel that order is important
        log(maxright + " go left at " + T)
        maxright = Math.max(maxright, traverseright(T.l))
      }
      log(maxright + " node " + T)
      maxright
    }

    Math.max(traverseleft(T), traverseright(T))
  }

  def solution2(T: Tree): Int = {
    def amplitude(T: Tree, highestprevious: Int, lowestprevious: Int): Int = {
      var max = 0
      if (T == null) return 0

      /*
      if (T.l != null) {
        log("go left at " + T)
        //max = amplitude(T.l, Math.max(highestprevious, T.x))
      }
      if (T.r != null) {
        log("go right at " + T)
        //max = amplitude(T.r, Math.max(highestprevious, T.x))
      }
      
      log("node " + T)
      * 
      */

      val newhighest = Math.max(highestprevious, T.x)
      val newlowest = Math.min(lowestprevious, T.x)

      if (T.r == null && T.l == null) { // a real leaf node
        Math.abs(newlowest - newhighest)
      } else {
        Math.max(amplitude(T.l, newhighest, newlowest), amplitude(T.r, newhighest, newlowest))
      }
    }

    amplitude(T, T.x, T.x)
  }

  def solution(T: Tree): Int = {
    def countvisibile(T: Tree, value: Int): Int = {
      if (T == null) {
        0
      } else if (T.x < value) {
        countvisibile(T.l, value) + countvisibile(T.r, value)
      } else {
        1 + countvisibile(T.l, value) + countvisibile(T.r, value)
      }
      /*
      if (T.l != null) {
        log("go left at " + T)
        traverse(T.l, value)
      }
      if (T.r != null) {
        log("go right at " + T)
        traverse(T.r, value)
      }
      log("node " + T)
      1
      * 
      */

    }
      
    if (T == null) -1
    else if (T.l == null && T.r == null) 0
    else countvisibile(T, T.x)
  }

  def main(args: Array[String]): Unit = {

    val test1 = new Tree(5, new Tree(3, null, null),
      new Tree(10, new Tree(12, new Tree(21, null, null), new Tree(20, null, null)), null))

    val test2 = new Tree(5, new Tree(8, new Tree(12, null, null), new Tree(2, null, null)),
      new Tree(9, new Tree(7, new Tree(1, null, null), null), new Tree(4, new Tree(3, null, null), null)))

    val test3 = new Tree(5, new Tree(3, new Tree(20, null, null), new Tree(21, null, null)),
      new Tree(10, new Tree(1, null, null), null))

    val test4 = new Tree(8, new Tree(2, new Tree(8, null, null), new Tree(7, null, null)),
      new Tree(6, null, null))

    val test5 = new Tree(5, new Tree(8, new Tree(12, null /* new Tree(11, null, null) */ , null), new Tree(2, null, null)),
      new Tree(9, new Tree(7, new Tree(1, null, null), null), new Tree(4, new Tree(3, null, null), new Tree(13, null, new Tree(3, null, null)))))

    val test6 = new Tree(5, new Tree(8, new Tree(12, new Tree(11, null, null), null), new Tree(2, null, null)),
      new Tree(9, new Tree(7, new Tree(1, null, null), 
          new Tree(19, null, new Tree(191, null, new Tree(192, null, new Tree(193, null, new Tree(194, null, null)))))), 
          new Tree(4, new Tree(3, null, null), new Tree(13, null, new Tree(3, null, null)))))

    val test7 = new Tree(1, null, null)
    
    val alltests = Array(test1, test2, test3, test4, test5, test6, test7, null)
    //val alltests = Array(test3, test4, test7, null)

    for (test <- alltests) {
      println("-------------------")
      //println(solution1(test) + " using " + test)
      //println(solution2(test) + " using " + test)
      println(solution(test) + " using " + test)

    }

    //println(test4)
  }

  def log(a: Any) {
    if (true) { // poor mans logging
      println(a)
    }
  }
}

class Tree(var x: Int, var l: Tree, var r: Tree) {
  // muhahahah, create a way to write my own test case inputs
  def toString(T: Tree): String = {
    if (T == null) "None"
    else "(" + T.x + ", " + toString(T.l) + ", " + toString(T.r) + ")"
  }

  override def toString(): String = {
    toString(this)
  }
}
