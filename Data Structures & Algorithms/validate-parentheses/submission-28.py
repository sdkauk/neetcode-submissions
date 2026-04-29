class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}' : '{', ')' : '(', ']' : '['}
        stack = []
        for char in s:
            if char not in closeToOpen:
                stack.append(char)
                continue
            if not stack:
                return False
            if closeToOpen[char] != stack.pop():
                return False
        if not stack:    
            return True
        return False