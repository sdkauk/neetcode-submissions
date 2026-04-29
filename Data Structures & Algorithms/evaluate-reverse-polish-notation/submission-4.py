class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y) # because we're truncating it
        }
        operators = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()
                result = operations[token](x, y)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()
            
