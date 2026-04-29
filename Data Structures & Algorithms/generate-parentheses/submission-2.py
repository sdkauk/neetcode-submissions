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
                op += 1
                backtrack(op, cp)
                stack.pop()
                op -= 1
            
            if op > cp:
                stack.append(")")
                cp += 1
                backtrack(op, cp)
                stack.pop()
                cp -= 1
            
        backtrack(0,0)
        return output


