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

    /*
     * Complete the 'miniMaxSum' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void miniMaxSum(List<Integer> arr) {
    // Write your code here
        Collections.sort(arr);
        BigInteger sum = new BigInteger("0");
        for (int i = 0; i < arr.size(); i++) {
			sum = sum.add(new BigInteger(String.valueOf(arr.get(i))));
		}
        System.out.println(new BigInteger(String.valueOf(sum)).subtract(new BigInteger(String.valueOf(Collections.max(arr))))+" "+new BigInteger(String.valueOf(sum)).subtract(new BigInteger(String.valueOf(Collections.min(arr)))));

}}

public class hackerrank1 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.miniMaxSum(arr);

        bufferedReader.close();
    }
}
