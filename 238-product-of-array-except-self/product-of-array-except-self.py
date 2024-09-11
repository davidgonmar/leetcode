class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        index = 1
        curr = 1 
        while index < len(nums): 
            curr *= nums[index - 1]
            res[index] = curr
            index += 1

        curr = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= curr
            curr = curr * nums[i]
        return res


