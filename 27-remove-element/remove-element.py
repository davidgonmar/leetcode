class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        while count < len(nums):
            print(count, nums[count])
            if nums[count] == val:
                nums.pop(count)
            else:
                count +=1
        return count