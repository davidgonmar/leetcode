import java.util.Map;
import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> auxMap = new HashMap<>();
        for(Integer i=0; i<nums.length; i++){
            if (auxMap.containsKey(target - nums[i])){
                return new int[] {auxMap.get(target - nums[i]), i};
            }
            auxMap.put(nums[i], i);
        }
        return new int[]{};
    }
}