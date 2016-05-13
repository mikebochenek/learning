---
layout: post
title:  "Apache Spark and MySQL"
date:   2016-05-13 17:15:31
categories: coding
---

BigData and Data Science is all the hype these days.  I had played around with Apache Spark before and read a few books.  I wanted to see how quickly I could read data from MySQL and try some (highly advanced) operations on the resulting data.

## scala code
{%highlight scala %}
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.functions._

object RDDRelationMySQL {
  def main(args: Array[String]) {
    val startTS = System.currentTimeMillis
    
    val url = "jdbc:mysql://localhost:3306/presto?user=prestouser&password=password"

    val sparkConf = new SparkConf().setAppName("RDDRelation").setMaster("local")
    val sc = new SparkContext(sparkConf)
    val sqlContext = new SQLContext(sc)

    // Importing the SQL context gives access to all the SQL functions and implicit conversions.
    import sqlContext.implicits._

    val restaurants = sqlContext.jdbc(url, "restaurant")
    val dishes = sqlContext.jdbc(url, "dish")
    val users = sqlContext.jdbc(url, "user")
    val friends = sqlContext.jdbc(url, "friend")
    val tags = sqlContext.jdbc(url, "tag")
    val likes = sqlContext.jdbc(url, "activity_log").filter("activity_type = 11")
    
    println ("restaurants RDD size: " + restaurants.collectAsList().size())
    println ("dish RDD size: " + dishes.collectAsList().size())
    println ("users RDD size: " + users.collectAsList().size())
    println ("friends RDD size: " + friends.collectAsList().size())
    println ("tags RDD size: " + tags.collectAsList().size())
    println ("likes RDD size: " + likes.collectAsList().size())

    likes.foreach { x => println(x) }
    
    println ("done in: " + (System.currentTimeMillis - startTS))
    sc.stop()
  }
}
{%endhighlight%}



## pom.xml

{%highlight bash %}
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>sparktest</groupId>
	<artifactId>sparktest</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<build>
		<sourceDirectory>src</sourceDirectory>
		<plugins>
			<plugin>
				<artifactId>maven-compiler-plugin</artifactId>
				<version>3.3</version>
				<configuration>
					<source>1.8</source>
					<target>1.8</target>
				</configuration>
			</plugin>
		</plugins>
	</build>
	<dependencies>
		<dependency>
			<groupId>org.apache.spark</groupId>
			<artifactId>spark-core_2.10</artifactId>
			<version>1.6.1</version>
		</dependency>
		<dependency>
			<groupId>org.apache.spark</groupId>
			<artifactId>spark-sql_2.10</artifactId>
			<version>1.3.0</version>
		</dependency>
		<dependency>
			<groupId>org.apache.spark</groupId>
			<artifactId>spark-mllib_2.10</artifactId>
			<version>1.3.0</version>
		</dependency>
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<version>5.1.12</version>
		</dependency>
	</dependencies>
</project>
{%endhighlight%}

## Helpful links and resources:

- [Spark SQL, DataFrames and Datasets Guide](http://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Using Apache Spark and MySQL for Data Analysis](https://www.percona.com/blog/2015/10/07/using-apache-spark-mysql-data-analysis/)
