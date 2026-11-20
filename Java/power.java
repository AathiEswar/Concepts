import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    public static String timeConversion(String s) {
    // Write your code here
    String[] spl = s.split(":");
    if(spl[2].charAt(2) == 'P'){
        s = (spl[0].equals("12"))?"12"+s.substring(2,8):String.valueOf(Integer.valueOf(spl[0])+12)+s.substring(2,8);
    }
    else{
        s = (spl[0].equals("12"))?"00"+s.substring(2, 8):s.substring(0,8);
    }
    return s;

    }

}

public class power {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();

        String result = Result.timeConversion(s);
        System.out.println(result);
    }
}
