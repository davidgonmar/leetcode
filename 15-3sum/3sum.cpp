class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int curr = 0; curr < nums.size(); curr++) {
            if (curr > 0 && nums[curr] == nums[curr - 1]) continue;
            int l = curr + 1;
            int r = nums.size() - 1;
            while (l < r) {
                int sum = nums[curr] + nums[l] + nums[r];
                if (sum == 0) {
                    res.push_back({nums[curr], nums[l], nums[r]});
                    while (l < r && nums[l] == nums[l+ 1]) ++l;
                    while (l < r && nums[r] == nums[r - 1]) --r;
                    r--;
                    l++;
                } else if (sum > 0) {
                    r--;
                } else { // sum < 0
                    l++;
                }
            }
        }

        return res;
    }
};