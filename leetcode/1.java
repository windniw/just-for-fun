public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        for (int i=0;i<nums.length-1;++i)
        for (int j=i+1;j<nums.length;++j)
        if (nums[i] + nums[j] == target){
            res[0] = i;
            res[1] = j;
            return res;
        }
        return null;
    }
}

//-------------------

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        HashMap<Integer, Integer> h = new HashMap<>();
        for (int i=0;i<nums.length;++i){
            h.put(nums[i], i);
        }
        for (int i=0;i<nums.length;++i){
            if (h.containsKey(target-nums[i])){
                if (h.get(target-nums[i]) == i) continue;
                res[0] = h.get(target-nums[i]);
                res[1] = i;
                return res;
            }
        }
        return null;
    }
}
