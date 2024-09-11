class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = False
        curr = ""
        for sub in reversed(s):
            if sub is not " ":
                word = True
                curr += sub
            else:
                if word == True:
                    return len(curr)
        return len(curr)

        