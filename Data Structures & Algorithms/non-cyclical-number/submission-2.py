class Solution:
    def isHappy(self, n: int) -> bool:
        self.results = []
        return self.summation(n)
    

    def summation(self, n: int) -> int | bool:
        lst = []
        for c in str(n):
            lst.append(c)
        entry = 0
        for elem in lst:
            entry += int(elem)**2
        if entry == 1:
            return True
        elif entry in self.results:
            return False
        self.results.append(entry)
        return self.summation(entry)
        

        