class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')' : '(', '}' : '{', ']' : '['}

        stack = []
        for char in s:
            if char in brackets and not stack:
                return False
            if char not in brackets:
                stack.append(char)
            else:
                opening = stack[-1]
                if brackets[char] == opening:
                    stack.pop()
                else:
                    return False
        if stack:
            return False

        return True
