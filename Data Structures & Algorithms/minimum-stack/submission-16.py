class MinStack:

    def __init__(self):
        self.vals = []
        self.minvals = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        if self.minvals:
            val = min(self.minvals[-1], val)
        self.minvals.append(val)

    def pop(self) -> None:
        self.vals.pop()
        self.minvals.pop()

    def top(self) -> int:
        return self.vals[-1]
        

    def getMin(self) -> int:
        return self.minvals[-1]
        
