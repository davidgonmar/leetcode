class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        while p2 >= p1:
            half = (p1 + p2)//2
            if nums[half] == target:
                return half
            if nums[half] > target:
                p2 = half - 1
            else:
                p1 = half + 1
        return -1
