// http://web.cs.ucla.edu/~linmanna/cs239/

class SimpleCSVHeader(header:Array[String]) extends Serializable {
  val index = header.zipWithIndex.toMap
  def apply(array:Array[String], key:String):String = array(index(key))
}

import org.apache.spark.SparkContext
import org.apache.spark.mllib.tree.DecisionTree
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.tree.configuration.Algo._
import org.apache.spark.mllib.tree.impurity.Variance

// Load and parse the training data file
val csv = sc.textFile("/home/mike/data/winton/train1000.csv")
val data = csv.map(line => line.split(",").map(elem => (if (elem == "") "0.0" else elem.trim)))  /* 1 fix for java.lang.NumberFormatException: empty String */
val header = new SimpleCSVHeader(data.take(1)(0)) 
val rows = data.filter(line => header(line,"Id") != "Id") // filter the header out

val parsedData = rows.map { line =>
  val parts = line.map(_.toDouble)
  LabeledPoint(parts(0), Vectors.dense(parts.take(26))) /* this is actually LabeledPoint(label: Double, features: Array[Double]), but take(26) is actually wrong */
}

// Run training algorithm to build the model
val maxDepth = 5
val model = DecisionTree.train(parsedData, Regression, Variance, maxDepth)

// Evaluate model on training examples and compute training error
val valuesAndPreds = parsedData.map { point =>
  val prediction = model.predict(point.features)
  (point.label, prediction)
}
val MSE = valuesAndPreds.map{ case(v, p) => math.pow((v - p), 2)}.mean()
println("training Mean Squared Error = " + MSE)

valuesAndPreds.take(6)
// oh... this is not what we are really looking for, is it..?

// Load and parse the ACTUAL TEST data file
val csvREAL = sc.textFile("/home/mike/data/winton/test.csv")
val dataREAL = csvREAL.map(line => line.split(",").map(elem => (if (elem == "") "0.0" else elem.trim)))  /* 1 fix for java.lang.NumberFormatException: empty String */
val headerREAL = new SimpleCSVHeader(dataREAL.take(1)(0)) 
val rowsREAL = dataREAL.filter(line => headerREAL(line,"Id") != "Id") // filter the header out

/* val realValue = rowsREAL.map { point =>
  val prediction = model.predict(point.features)
  (point.label, prediction)
} but this seems somehow wrong... how do we it tell it what to predict magically... ?  */
