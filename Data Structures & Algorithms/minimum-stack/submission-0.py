class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        self.min_s.append(min(val, val if not self.min_s else self.min_s[-1]))
        

    def pop(self) -> None:
        self.s.pop()
        self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]


    def getMin(self) -> int:
        return self.min_s[-1]