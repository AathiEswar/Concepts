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

class Result{
    public static String sortRow(String ele){
        char[] arr = ele.toCharArray();
        Arrays.sort(arr);
        return new String(arr);
    }
   
    public static String gridChallenge(List<String> grid) {
        int n = grid.size();
        for(int i=0;i<grid.size();i++){
            String ele = sortRow(grid.get(i));
            grid.set(i, ele);
        }
        for(int i = 0;i<n-1;i++){
            if(grid.get(i).compareTo(grid.get(i+1)) >0){
                return "NO";
            }
        }
                return "YES";
        }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int t = Integer.parseInt(sc.nextLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            
                int n = Integer.parseInt(sc.nextLine().trim());

                List<String> grid = IntStream.range(0, n).mapToObj(i -> {
                   
                        return sc.nextLine();
                    }
                )
                    .collect(toList());


                String result = Result.gridChallenge(grid);


            } 
        );  

    }
}
