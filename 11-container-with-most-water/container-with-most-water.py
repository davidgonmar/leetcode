class Solution:
    def maxArea(self, height: List[int]) -> int:
        currMax = 0
        ptr1 = 0
        ptr2 = len(height) - 1

        while (ptr1 != ptr2):
            height1 = height[ptr1]
            height2 = height[ptr2]
            currMax = max(currMax, (ptr2 - ptr1)*min(height1, height2))
            if height1 < height2:
                ptr1 +=1
            else:
                ptr2 -=1

        return currMax