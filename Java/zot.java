public class zot {
    public static void main(String[] args) {
        int[] arr = {1,0,2,2,2,1,0};
        int n = arr.length;
        sortarr(arr, n);
        for(int ele : arr)
            System.out.println(ele);
        
    }
    public static void swap(int[] arr,int i,int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

    }
    static void sortarr(int[] arr,int n)
    {
        int i=0, j=0, k=n-1;
        while(i<=k)
        {
            if(arr[i] == 0)
            {
                swap(arr, i, j);
                i++;
                j++;
            }
            else if(arr[i] == 2)
            {
                swap(arr, i, k);
                k--;
            }
            else
            {
                i++;
            }
        }
        
    }
}
