class MinStack:

    def __init__(self):
        self.stack = []
        self.stackmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stackmin or val < self.stackmin[-1]:
            self.stackmin.append(val)
        else:
            self.stackmin.append(self.stackmin[-1])
        return 

    def pop(self) -> None:
        self.stack.pop()
        self.stackmin.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmin[-1]
        
