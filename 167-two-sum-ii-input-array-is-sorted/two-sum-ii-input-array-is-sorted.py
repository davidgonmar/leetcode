class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers) - 1

        while (ptr1 != ptr2):
            _sum = numbers[ptr1] + numbers[ptr2]
            if _sum == target: 
                return [ptr1 + 1, ptr2 + 1]
            elif _sum > target:
                ptr2 -= 1
            else:
                ptr1 += 1
        
        return []