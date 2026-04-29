class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', '}':'{', ']':'['}
        stack = []
        for i, char in enumerate(s):
            if char in closeToOpen:
                if not stack:
                    return False
                if stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack