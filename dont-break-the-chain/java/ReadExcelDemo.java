package com.howtodoinjava.demo.poi;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.*;
import java.nio.charset.Charset;
import java.util.Iterator;

/**
 * http://howtodoinjava.com/2013/06/19/readingwriting-excel-files-in-java-poi-tutorial/
 */
public class ReadExcelDemo
{
    public static void main(String[] args) {
        ReadExcelDemo demo = new ReadExcelDemo();
        try {
            demo.loadTemplate();
            demo.processExcel();
        } catch (Exception e) {
            System.err.println(e);
        }
    }

    public void processExcel() throws Exception {
        String filepath = "/tmp/x_100114.xlsx";
        FileInputStream file = new FileInputStream(new File(filepath));

        XSSFWorkbook workbook = new XSSFWorkbook(file); //Create Workbook instance holding reference to .xlsx file
        XSSFSheet sheet = workbook.getSheetAt(0); //Get first/desired sheet from the workbook

        Iterator<Row> rowIterator = sheet.iterator(); //Iterate through each rows one by one
        while (rowIterator.hasNext())
        {
            Row row = rowIterator.next();

            Iterator<Cell> cellIterator = row.cellIterator(); //For each row, iterate through all the columns

            String desc = "";
            String samtechid = "";
            while (cellIterator.hasNext())
            {
                Cell cell = cellIterator.next();
                if (cell.getColumnIndex() == 7) {
                    desc = cell.getStringCellValue().trim();
                }
                if (cell.getColumnIndex() == 8) {
                    samtechid = cell.getStringCellValue().trim();
                }
            }

            if (desc != null && desc.trim().length() > 0 && samtechid != null && samtechid.trim().length() > 0) {

//                /desc = desc.replaceAll("&", "&"); //TODO
                for (String line : template) {
                    //line = line.replaceAll("", desc);
                    if (line != null) {
                        line = line.replaceAll("1075", samtechid);
                        System.out.println(line);
                    }
                }
            }

            //System.out.println(samtechid);

            // replace...
            //TODO do I need to escape any special characters from the  descriptions? ampersand?

        }
        file.close();
    }

    private String[] template = new String[90];
    public void loadTemplate() throws Exception{
        String line;
        String filepath = "/tmp/inserts_template.sql";

        InputStream fis = new FileInputStream(filepath);
        BufferedReader br = new BufferedReader(new InputStreamReader(fis, Charset.forName("UTF-8")));
        int i = 0;
        while ((line = br.readLine()) != null) {
            if (line != null /* && line.trim().length() > 0*/ ) {
                template[i++] = line;
                //System.out.println(line);
            }
        }

        br.close();
        br = null;
        fis = null;
    }
}

/*
    <dependencies>
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi</artifactId>
            <version>3.8</version>
        </dependency>
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi-ooxml</artifactId>
            <version>3.8</version>
            <exclusions>
                <exclusion>
                    <groupId>stax</groupId>
                    <artifactId>stax-api</artifactId>
                </exclusion>
                <exclusion>
                    <groupId>xml-apis</groupId>
                    <artifactId>xml-apis</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
    </dependencies>
*/
