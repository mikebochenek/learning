package topcoder

import org.junit.Test
import org.junit.Assert._

/**
 * Fernando loves to play chess. One day he decided to play chess on an unusually
 * large rectangular board. To compensate for the board's size he also decided to
 * change the distance a knight can move in a single jump.
 *
 * To describe the moves easily, we will now introduce a coordinate system.
 * Each cell of the chessboard can be described using two integers (r,c): its
 * row number and its column number. Now, if we have a piece at (r,c), the move
 * (x,y) takes the piece to the cell (r+x,c+y).
 *
 * The new chess piece will be called an (a,b)-hyperknight. The hyperknight always
 * has 8 possible moves: (+a,+b), (+a,-b), (-a,+b), (-a,-b), (+b,+a), (+b,-a),
 * (-b,+a), and (-b,-a). Note that the original chess knight is a (2,1)-hyperknight.
 *
 * Of course, as the chessboard is finite, it is not always possible to make each
 * of the 8 moves. Some of them may cause our hyperknight to leave the chessboard.
 * A move is called valid if the destination cell is on the chessboard.
 * Fernando would like to know the number of cells on his board such that his
 * hyperknight will have exactly k valid moves from that cell.
 *
 * You are given the ints a, b, numRows, numColumns and k. The values numRows and
 * numColumns define the number of rows and number of columns on the chessboard,
 * respectively. The other three values were already explained above. Compute and
 * return the number of cells on the chessboard that have exactly k valid (a,b)-hyperknight moves.
 *
 * Notes
 * -	If you wish, you may assume that the rows are numbered 0 through numRows-1 and
 * 		columns 0 through numColumns-1. However, note that the actual row/column numbers
 *   	do not matter, as long as they are consecutive.
 * Constraints
 * -	a will be between 1 and 1,000,000,000 (10^9), inclusive.
 * -	b will be between 1 and 1,000,000,000 (10^9), inclusive.
 * -	a will not be equal to b.
 * -	numRows will be between 1 and 1,000,000,000 (10^9), inclusive.
 * -	numColumns will be between 1 and 1,000,000,000 (10^9), inclusive.
 * -	2*max(a,b) will be strictly less than min(numRows,numColumns).
 * -	k will be between 0 and 8, inclusive.
 */
class HyperKnight {

  // maybe start with naive approach, and adjust for performance later
  // maybe we should instead check for invalid?
  def countCells(a: Int, b: Int, numRows: Int, numColumns: Int, k: Int): Long = {

    def countValid(x: Int, y: Int): Int = {
      
      def isValid(fx: Int, fy: Int): Int = {
        if (fx >= 0 && fy >= 0 && fx < numRows && fy < numColumns) 1
        else 0
      }

      val rt = isValid(x + a, y + b) +
        isValid(x + a, y - b) +
        isValid(x - a, y + b) +
        isValid(x - a, y - b) +
        isValid(x + b, y + a) +
        isValid(x + b, y - a) +
        isValid(x - b, y + a) +
        isValid(x - b, y - a)

      // println (x + "," + y + " has " + rt)

      rt
    }

    var count = 0
    
    for (i <- 0 to numRows - 1) {
      for (j <- 0 to numColumns - 1) {
        if (countValid(i, j) == k) { count = count + 1 }
      }
    }

    count
  }

  @Test def test0() { assertEquals(20, countCells(2, 1, 8, 8, 4)) }
  @Test def test1() { assertEquals(16, countCells(3, 2, 8, 8, 2)) }
  @Test def test2() { assertEquals(0, countCells(1, 3, 7, 11, 0)) }
  @Test def test3() { assertEquals(56, countCells(3, 2, 10, 20, 8)) }
  @Test def test4() { assertEquals(564, countCells(1, 4, 100, 10, 6)) }
  //@Test def test5() { assertEquals(999999988000000036L, countCells(2, 3, 1000000000, 1000000000, 8))}
}