import java.util.Scanner;


public class Solution {
    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        String s = scan.next();                
        
        String ans = "";        
        for(int i = 0; i< s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isUpperCase(c)) {
                ans += Character.toLowerCase(c);
            } else {
                ans += Character.toUpperCase(c);
            }
        }
        
        System.out.println(ans);        
    }
}