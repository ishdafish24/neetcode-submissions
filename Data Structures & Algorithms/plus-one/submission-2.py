class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits)-i-1))
        num += 1
        lst = []
        decomp = num
        while decomp > 0:
            lst.append(decomp % 10)
            decomp = decomp // 10
        lst.reverse()
        return lst