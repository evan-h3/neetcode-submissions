class MinStack:

    def __init__(self):
        self.s = []
        self.minS = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.minS or val <= self.minS[-1]:
            self.minS.append(val)

    def pop(self) -> None:
        val = self.s.pop()
        if self.minS[-1] == val:
            self.minS.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minS[-1]


