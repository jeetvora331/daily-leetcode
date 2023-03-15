class MinStack:

    def __init__(self):
        self.stack = []
        self.minS = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minS :
            mini = val
        else:
            mini = self.minS[-1]
            mini = min(mini , val)
        self.minS.append(mini)
          
    def pop(self) -> None:
        self.stack.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minS[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()