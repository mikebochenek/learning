package xml

import org.custommonkey.xmlunit._;
import org.xml.sax.SAXException;

import javax.xml.parsers.ParserConfigurationException;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.List;

object CompareMainframeXMLs {

  val dir1 = "/tmp/lam_v2d"
  val dir2 = "/tmp/lam_v1d"

  var comparedFiles = 0
  var diffCount = 0
  var similarFileCount = 0

  def main(args: Array[String]): Unit = {
    val startTs = System.currentTimeMillis();

    val aFile = new File(dir1);
    if (aFile.isDirectory()) {
      val listOfFiles: Array[File] = aFile.listFiles();

      println(" start compare for " + dir1 + "  " + listOfFiles.length + " files.");
      if (listOfFiles != null) {
        for (i <- 0 until listOfFiles.length) {
          val name = listOfFiles(i).getName();
          if (name.startsWith("log-A2") && new File(dir2 + name).exists()) {
            comparedFiles = comparedFiles + 1;
            compare(name);
          }
        }
      }
    }

    println("compared " + comparedFiles + " files in " + (System.currentTimeMillis() - startTs)
      + "ms - " + similarFileCount + " similar files  - " + diffCount + " total diffs");

  }

  def compare(filename: String) {
    var fr1: FileReader = null;
    var fr2: FileReader = null;
    try {
      fr1 = new FileReader(dir1 + filename);
      fr2 = new FileReader(dir2 + filename);
    } catch {
      case e: FileNotFoundException => e.printStackTrace();
    }

    try {
      XMLUnit.setIgnoreWhitespace(true);
      XMLUnit.setIgnoreComments(true);
      XMLUnit.setIgnoreAttributeOrder(true);

      var diff = new Diff(fr1, fr2);

      var detDiff = new DetailedDiff(diff);

      detDiff.overrideElementQualifier(new ElementNameAndAttributeQualifier()); // this ignores order in XML elements

      var differences = detDiff.getAllDifferences();
      var hasValidDiffs = false;
      for (i <- 0 until differences.size()) { //difference: Difference <- differences) {
        val difference = (differences.get(i)).asInstanceOf[Difference]; 
        /** this is how you do casts in Scala */

        if (isMinorDifference(difference)) {
          // we ignore minor / accepted differences
        } else {
          diffCount = diffCount + 1;
          if (!hasValidDiffs) System.out.println(" ------------------------ diffs found in " + filename + " -------------------------- ");
          hasValidDiffs = true;
          println(difference);
        }
      }

      if (!hasValidDiffs) {
        similarFileCount = similarFileCount + 1;
      }

    } catch {
      case se: SAXException => se.printStackTrace();
      case ioe: IOException => ioe.printStackTrace();
    } /** this is how you catch exceptions in scala */
  }

  def isMinorDifference(difference: Difference): Boolean = {
    if ("/message[1]/header[1]/requestId[1]/text()[1]".equals(difference.getControlNodeDetail().getXpathLocation())
      || "/message[1]/header[1]/timestamp[1]/text()[1]".equals(difference.getControlNodeDetail().getXpathLocation())) {
      // we can ignore requestId and timestamp");
      return true;
    }

    if (difference.toString().contains("/message[1]/body[1]/INIADI[1]/@iniName")) {
      //TODO we can ignore this for now, since we have 7947
      return true;
    }

    if ("sequence of child nodes".equals(difference.getDescription()) && difference.isRecoverable()) {
      // we can ignore recoverable sequence issues...
      return true;
    }

    if ((difference.getDescription().startsWith("Expected number of child nodes")
      && difference.toString().contains(" comparing <groups...>")
      || difference.getDescription().startsWith("Expected presence of child node 'group'"))
      || difference.toString().contains(" comparing <groups...>")
      || difference.toString().contains(" comparing <group...>")) {
      // all group differences can be ignored
      return true;
    }

    return false;
  }
}
