class MinStack:

    def __init__(self):
        self.stack = []
        self.minValueStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minValueStack) > 0 and val >= self.minValueStack[-1]:
            self.minValueStack.append(self.minValueStack[-1])
        else:
            self.minValueStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minValueStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minValueStack[-1]


        
