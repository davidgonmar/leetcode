class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 0
        while i < len(s) - 1:
            if s[i] == "0" and s[i+1] == "1":
                return False
            i += 1
        return True