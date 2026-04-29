class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}': '{', ']': '[', ')': '('}
        stack = []

        for char in s:
            if char in brackets:
                if not stack:
                    return False
                if brackets[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False
