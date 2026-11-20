public class demo3 {
    public static void main(String[] args) {
        String input = "i! love: zoho";
        StringBuilder sb = new StringBuilder("");
        
        char[] characterArray = new char[input.length()];
        for(int i = 0; i<input.length(); i++){
            if(isNumberOrAlphabet(input.charAt(i))){
                characterArray[i] = input.charAt(i);
            }
        }
        System.out.println(input);
        System.out.println(characterArray);
        int j = characterArray.length;
        
//        String stringResult = new String(characterArray);
//        System.out.printf("%s",stringResult);

        for(int i = 0; i < input.length(); i++){
    

            
            if(isNumberOrAlphabet(input.charAt(i))){
                sb.append(characterArray[j]);
                j--;
            }
            else{
                sb.append(characterArray[i]);
                i++;
            }
        
        }
        System.out.println(sb);
    }
    public static boolean isNumberOrAlphabet(char letter){
        return Character.isDigit(letter) || Character.isAlphabetic(letter);
    }
}