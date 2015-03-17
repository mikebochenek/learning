package zoo;

import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

/**
 * 1/29/15 en_US
 * 29.01.15 de_CH
 * 29.01.15 fr_CH
 * 29.01.15 it_CH
 * 29/01/15 fr_FR
 */
public class TestFormatter {
    public static void main(String[] args) {
        printShortDate(new Locale("en", "US"));
        printShortDate(new Locale("de", "CH"));
        printShortDate(new Locale("fr", "CH"));
        printShortDate(new Locale("it", "CH"));
        printShortDate(new Locale("fr", "FR"));
    }



    private static void printShortDate(Locale currentLocale) {
        Date today;
        String dateOut;
        DateFormat dateFormatter;

        dateFormatter = DateFormat.getDateInstance(DateFormat.SHORT, currentLocale);
        today = new Date();
        dateOut = dateFormatter.format(today);

        System.out.println(dateOut + " " + currentLocale.toString());
    }

}
