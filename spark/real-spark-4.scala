// http://web.cs.ucla.edu/~linmanna/cs239/

class SimpleCSVHeader(header:Array[String]) extends Serializable {
  val index = header.zipWithIndex.toMap
  def apply(array:Array[String], key:String):String = array(index(key))
}

import org.apache.spark.SparkContext
import org.apache.spark.mllib.classification.NaiveBayes
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

// Split data into training (60%) and test (40%).
val splits = parsedData.randomSplit(Array(0.6, 0.4), seed = 11L)
val training = splits(0)
val test = splits(1)

val model = NaiveBayes.train(training, lambda = 1.0)

/* OK, now we know we can not really go on with Bayes ... 
 * Caused by: org.apache.spark.SparkException: Naive Bayes requires nonnegative feature values but 
 * found [501.0,0.0,-0.6593105882402971,0.5740347170012103,0.6341612364128077,9.0,0.11276214036754136,14653.0,0.2087,13.0,5.0,-0.8030557506734086,0.05,3.0,1.9158053223169804,0.36309177,1.0,-0.7466807239034332,0.8830097310997314,-1.3127450930161295,0.0,0.5556164150880708,-1.396229384288504,0.9333145496081694,-1.4205356821641444,-0.5716785266804119].
 */
val predictionAndLabel = test.map(p => (model.predict(p.features), p.label))
val accuracy = 1.0 * predictionAndLabel.filter(x => x._1 == x._2).count() / test.count()

