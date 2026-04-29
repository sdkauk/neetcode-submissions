class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int):
        self.stack.append(val)
        if self.mins and self.mins[-1] < val:
            self.mins.append(self.mins[-1])
        else:
            self.mins.append(val)

    def pop(self):
        self.mins.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        minval = self.mins[-1]
        return minval