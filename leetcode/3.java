public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int vis[] = new int[300];
        for (int i=0;i<300;++i) vis[i] = -1;
        int l = 0, res = 0;
        for (int i=0;i<s.length();++i){
            if (vis[s.charAt(i)] != -1 && l<=vis[s.charAt(i)]){
                l = vis[s.charAt(i)]+1;
            } 
            vis[s.charAt(i)] = i;
            res = res > i - l + 1 ? res : i - l + 1; 
        }
        return res;
    }
}
