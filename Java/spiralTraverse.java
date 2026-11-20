import java.util.*;
 
class spiralTraverse{
    static int R = 3;
    static int C = 4;
 
    static void print(int arr[][], int i, int j, int m, int n)
    {
        
       if(i >= m ||j >= n )
       {
           return ;
       }
       for(int p = i;p<n;p++)
       {
           System.out.println(arr[i][p]);
       }
       for(int p = i+1 ;  p<m ;p++)
       {
           System.out.println(arr[p][n-1]);
       }
       if(m-1 != i)
       {
           for(int p = n-2 ; p>=i ; p--)
           {
               System.out.println(arr[m-1][p]);
           }
       }
       if(m-1 != j)
       {
           for(int p = m-2 ; p>j ; p--)
           {
               System.out.println(arr[p][j]);
           }
       }
       print(arr,i+1 , j+1 , m-1,n-1);
    }
     

    public static void main(String[] args)
    {
        int a[][] = { { 1, 2, 3, 4 },
                      { 5, 6, 7, 8 },
                      { 9, 10, 11, 12 }
                       };
 
        
        print(a, 0, 0, R, C);
    }
}