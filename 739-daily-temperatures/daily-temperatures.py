class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while (stack and temp > stack[-1][1]):
                st_idx, st_val = stack.pop()
                res[st_idx] = idx - st_idx
            stack.append((idx, temp))
        return res