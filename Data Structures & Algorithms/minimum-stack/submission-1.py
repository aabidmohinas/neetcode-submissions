class MinStack:

    def __init__(self):

        self.minimumStack = []
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        self.minimum = min(self.minimum, val)
        self.minimumStack.append(self.minimum)

    def pop(self) -> None:
        self.minimumStack.pop()
        self.minimum = self.minimumStack[-1] if self.minimumStack else float('inf')
        return self.stack.pop()

    def top(self) -> int:

        return self.stack[-1]

    def getMin(self) -> int:

        return self.minimumStack[-1]
