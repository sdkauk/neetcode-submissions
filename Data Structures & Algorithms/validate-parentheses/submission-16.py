class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in s:
            if char in brackets:
                stack.append(char)
            
            else:
                if not stack:
                    return False
                
                else:
                    top = stack.pop()
                    if brackets[top] != char:
                        return False
                
        if stack:
            return False
        
        else:
            return True
        