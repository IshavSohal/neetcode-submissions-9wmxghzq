class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None
        
    def push(self, val: int) -> None:
        if self.minVal != None:
            self.minVal = min(val, self.minVal)
        else:
            self.minVal = val
        
        self.stack.append((val, self.minVal))

    def pop(self) -> None:
        self.stack.pop()
        if(len(self.stack) == 0):
            self.minVal = None
        else:
            self.minVal = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.minVal
        



        
