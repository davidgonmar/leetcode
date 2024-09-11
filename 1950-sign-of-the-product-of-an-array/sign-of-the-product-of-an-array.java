class Solution {
    public int arraySign(int[] nums) {
        var count = 1;

        for (var n: nums){
            if (n == 0) return 0;
            var sign = n>0? 1 : -1;
            count*=sign;
        }
        return (count>0)? 1: -1;
    }
}