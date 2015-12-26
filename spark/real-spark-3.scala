/* Doing linear regression with lasso
 * 
 * The lasso is a shrinkage and selection method for linear regression. It minimizes the usual sum of squared 
 * errors, with a bound on the sum of the absolute values of the coefficients. It is based on the original 
 * lasso paper found at http://statweb.stanford.edu/~tibs/lasso/lasso.pdf.
 */ 
class SimpleCSVHeader(header:Array[String]) extends Serializable {
  val index = header.zipWithIndex.toMap
  def apply(array:Array[String], key:String):String = array(index(key))
}

import org.apache.spark.SparkContext
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.regression.LassoWithSGD
import org.apache.spark.mllib.regression.RidgeRegressionWithSGD

// Load and parse the data file
val csv = sc.textFile("/home/mike/data/winton/train1000.csv")
val data = csv.map(line => line.split(",").map(elem => (if (elem == "") "0.0" else elem.trim)))  /* 1 fix for java.lang.NumberFormatException: empty String */
val header = new SimpleCSVHeader(data.take(1)(0)) 
val rows = data.filter(line => header(line,"Id") != "Id") // filter the header out

val parsedData = rows.map { line =>
  val parts = line.map(_.toDouble)
  LabeledPoint(parts(0), Vectors.dense(parts.take(26))) /* this is actually LabeledPoint(label: Double, features: Array[Double]), but take(26) is actually wrong */
}

val model = LassoWithSGD.train(parsedData,100,0.02,2.0)

model.weights

val model = RidgeRegressionWithSGD.train(parsedData,100,0.02,2.0)

model.weights
