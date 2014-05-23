package excel

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io._;
import java.nio.charset.Charset;
import java.util.Iterator;
import java.util.Date;

object ReadExcelDemo {

  def main(args: Array[String]): Unit = {
    val startTS = System.currentTimeMillis();
    
    generateSQL()

    println("\n\n\n -- script generated in " + (System.currentTimeMillis - startTS) + "ms. on " + (new Date().toString()))
  }
  
  def generateSQL() {
    try {
      println(" -- This script inserts and updates into PAI18N "
    		  + "\n\n\n -- first a couple of (conditional) inserts ... \n"
    		  + "\n--spool PAD.log \n"
    		  + "SET ESCAPE ON \n"
    		  + "SET DEFINE OFF \n")

      loadTemplate("/tmp/inserts_template.sql");
      processExcel()

      println("\n\n\n -- and now the updates ... ")
      
      loadTemplate("/tmp/updates_template.sql");
      processExcel()

      println("spool off")    		  ;

    } catch {
      case e: Exception => println(e);
    }    
  }

  def processExcel() {
    val filepath = "/tmp/px_1x114.xlsx"
    var file = new FileInputStream(new File(filepath))

    // http://howtodoinjava.com/2013/06/19/readingwriting-excel-files-in-java-poi-tutorial/
    var workbook = new XSSFWorkbook(file) //Create Workbook instance holding reference to .xlsx file
    var sheet: XSSFSheet = workbook.getSheetAt(0) //Get first/desired sheet from the workbook

    var rowIterator = sheet.iterator(); //Iterate through each rows one by one
    
    while (rowIterator.hasNext()) {
      var cellIterator = rowIterator.next().cellIterator(); //For each row, iterate through all the columns

      var desc = "";
      var sandratechid = "";
      while (cellIterator.hasNext()) {
        var cell = cellIterator.next();
        if (cell.getColumnIndex() == 7) desc = cell.getStringCellValue().trim();
        if (cell.getColumnIndex() == 8) sandratechid = cell.getStringCellValue().trim();
      }

      if (desc != null && desc.trim().length() > 0
        && sandratechid != null && sandratechid.trim().length() > 0 && !"sandra_TECH_ID".equals(sandratechid)) {

        //                /desc = desc.replaceAll("&", "&"); //TODO
        //TODO do I need to escape any special characters from the  descriptions? ampersand?

        for (line: String <- template) {
          //line = line.replaceAll("", desc);
          if (line != null) {
            var newLine = line.replaceAll(".1500.", sandratechid);
            newLine = newLine.replaceAll("__DESC", desc);
            println(newLine);
          }
        }
      }
    }
    
    file.close();
  }

  var template: Array[String] = new Array[String](90);

  def loadTemplate(filepath: String) {
    template = new Array[String](90);
    var line: String = null
    var fis = new FileInputStream(filepath);
    var br: BufferedReader = new BufferedReader(new InputStreamReader(fis, Charset.forName("UTF-8")));
    var i = 0;
    do {
      if (line != null /* && line.trim().length() > 0*/ ) {
        template(i) = line;
        i = i + 1;
      }
      line = br.readLine()
    } while (line != null);

    br.close();
    br = null;
    fis = null;
  }
}
