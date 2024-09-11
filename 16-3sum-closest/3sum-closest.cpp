class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int best_sum = 0;
        int best_diff = INT_MAX;
        sort(nums.begin(), nums.end());
        for (int curr = 0; curr < nums.size(); curr++) {
            if (curr > 0 && nums[curr] < nums[curr -1]) continue;
            int l = curr + 1;
            int r = nums.size() - 1;
            while (l < r) {
                int sum = nums[curr] + nums[l] + nums[r];
                if (sum == target) return sum;
                int diff = abs(sum - target);
                if (diff < best_diff) {
                    best_sum = sum;
                    best_diff = diff;
                }
                if (sum > target) {
                    r--;
                } else { // sum < target
                    l++;
                }
            }
        }

        return best_sum;
    }
};