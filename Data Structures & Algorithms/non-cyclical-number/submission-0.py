class Solution:
    def summation(self, n: int) -> int:
        lst = []
        for c in str(n):
            lst.append(c)
        entry = 0
        for elem in lst:
            entry += int(elem)**2
        if entry == 1:
            return -1
        elif entry in self.results:
            return -2
        self.results.append(entry)
        return self.summation(entry)
    
    def isHappy(self, n: int) -> bool:
        self.results = []
        outcome = self.summation(n)
        if outcome == -1:
            return True
        else:
            return False
        

        