import java.util.Scanner;

public class pnz {
    static String posneg(int n)
    {
        return n>0? "Positive":(n==0?"zero":"Negative");
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println(posneg(sc.nextInt()));
        sc.close();
    }
    
}
