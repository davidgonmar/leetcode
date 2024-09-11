class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mem = set(nums)
        longest_seq = 0

        for n in mem:
                if (n - 1) not in mem:
                    i = n
                    while (i in mem):
                        i += 1
                    longest_seq = max(longest_seq, i - n)
            
        return longest_seq


      
