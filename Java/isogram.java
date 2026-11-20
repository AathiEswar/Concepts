import java.util.HashSet;
import java.util.Set;

public class isogram {
    public static void main(String[] args) {
        System.out.println(isIsogram("hello"));
    }
    static boolean isIsogram(String s)
    {
        boolean tf = true;
        char[] ch = s.toCharArray();
        Set<Character> chSet = new HashSet<Character>();
        for(Character c : ch)
        {
            if (chSet.contains(c))
            {
                tf = false;
            }
            else{
                chSet.add(c);
            }
        }
        return tf;
    }
}
