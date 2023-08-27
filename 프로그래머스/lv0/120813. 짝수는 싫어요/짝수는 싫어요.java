public class Solution {
    public int[] solution(int n) {
        
        int[] ans = new int[(n+1)/2];
        
        for (int i=1, k=0; i<=n; i+=2) {
            ans[k] = i;
            k++;
        }
        
        return ans;
    }
}
