public class reverseString {
    public static void main(String[] args) {
        String str = "i! love: zoho";
        char[] arr = str.toCharArray();
        int low = 0;
        int high = str.length() - 1;
        while (low < high) {
            if (!isNumberOrAlphabet(arr[low])) {
                low++;
            }
            if (!isNumberOrAlphabet(arr[high])) {
                high--;
            } else {
                swap(arr,low,high);
                low++;
                high--;

            }
        }
        String stringResult = new String(arr);
        System.out.printf("%s",stringResult);
    }

    public static boolean isNumberOrAlphabet(char letter) {
        return Character.isDigit(letter) || Character.isAlphabetic(letter);
    }

    public static void swap(char[] a, int i1, int i2) {
        char temp = a[i1];
        a[i1] = a[i2];
        a[i2] = temp;
    }
}