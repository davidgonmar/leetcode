class Solution:
    def isValid(self, s: str) -> bool:
        equiv = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(equiv[char])
            else:
                if len(stack) == 0:
                    return False
                if char == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        
        if len(stack) > 0:
            return False

        return True
