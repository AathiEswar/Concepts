import java.util.Scanner;

public class demo
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int diag1=0,diag2=0;
        int[][] a ;
        a = new int[n][n];
        for (int i = 0; i < n; i++) {
            for(int j = 0;j<n;j++)
            {
                a[i][j] = sc.nextInt();
            }

        }
            for(int j = 0;j<n;j++)
            {
                diag1 += a[j][j];
                diag2 += a[j][n-j-1];
            }
            int diff = Math.abs(diag1-diag2);
            System.out.println(diff);

    }
}