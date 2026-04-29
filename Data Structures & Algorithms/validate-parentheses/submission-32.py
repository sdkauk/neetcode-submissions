class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}' : '{', ')' : '(', ']' : '['}
        stack = []

        for char in s:
            if char in closeToOpen and not stack:
                return False
            if char in closeToOpen and closeToOpen[char] == stack.pop():
                continue
            stack.append(char)
        
        return not stack
