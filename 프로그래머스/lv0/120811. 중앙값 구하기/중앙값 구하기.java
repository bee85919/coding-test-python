import java.util.Arrays;

public class Solution {
    public int solution(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        int ans = (n/2);
        return arr[ans];
    }
}
