class MinStack:

    def __init__(self):
        self.stack = []
        self.stackmin=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stackmin:
            self.stackmin.append(val)
        else:
            self.stackmin.append(min(val, self.stackmin[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.stackmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmin[-1]
