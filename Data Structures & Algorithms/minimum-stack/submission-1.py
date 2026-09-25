class MinStack:

    def __init__(self):
        self.stack = []
        self.side_stack = [] # to keep track of min val

    def push(self, val: int) -> None:

        self.stack.append(val)
        if self.side_stack:
            self.side_stack.append(min(val, self.side_stack[-1]))
        else:
            self.side_stack.append(val)
        

    def pop(self) -> None:

        self.side_stack.pop()
        return self.stack.pop()


        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.side_stack[-1]

        
