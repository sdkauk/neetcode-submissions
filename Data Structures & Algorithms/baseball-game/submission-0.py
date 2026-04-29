class Solution:
    def calPoints(self, operations: List[str]) -> int:

        scores = []
        output = 0
        for op in operations:
            if op == "+":
                score = scores[-1] + scores[-2]
                scores.append(score)
                output += score
            elif op == "D":
                score = scores[-1] *  2
                scores.append(score)
                output += score
            elif op == "C":
                score = scores.pop()
                output -= score
            else:
                scores.append(int(op))
                output += int(op)
        
        return output
        

