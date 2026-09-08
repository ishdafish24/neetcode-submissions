class MinStack:
    def __init__(self):
        self.lst = []
        self.mins = []

    def push(self, val: int) -> None:
        self.lst.append(val)
        if self.mins == [] or self.mins[-1] >= val:
            self.mins.append(val)

    def pop(self) -> None:
        if self.lst[-1] == self.mins[-1]:
            self.mins.pop()
        self.lst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.mins[-1]
