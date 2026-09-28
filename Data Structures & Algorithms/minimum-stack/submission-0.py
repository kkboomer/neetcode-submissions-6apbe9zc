class MinStack:

    def __init__(self):
        self.s, self.low = [], []

    def push(self, val: int) -> None:
        #after we append, we have to figure out how do we update low
        self.s.append(val)
        if self.low:
            self.low.append(min(self.low[-1], val))
        else:
            self.low.append(val)

    def pop(self) -> None:
        # after we pop we must update the low
        self.s.pop()
        self.low.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        # depends on how we store low
        return self.low[-1]
