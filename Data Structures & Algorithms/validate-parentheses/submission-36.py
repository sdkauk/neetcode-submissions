class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {']' : '[', '}' : '{', ')' : '('}
        stack = []
        for char in s:
            if char in closeToOpen:
                if not stack:
                    return False
                if closeToOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        return True