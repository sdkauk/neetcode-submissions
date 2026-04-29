class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        output = []

        def backtrack(op, cp):
            if op == cp == n: #if the number of ( is equal to the number of ) and equal to n, then we have a our completed string
                output.append("".join(stack))
                return
            
            if op < n:
                stack.append("(")
                backtrack(op + 1, cp)
                stack.pop()
            
            if op > cp:
                stack.append(")")
                backtrack(op, cp + 1)
                stack.pop()
            
        backtrack(0,0)
        return output


