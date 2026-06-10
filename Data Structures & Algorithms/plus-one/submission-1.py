class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            ind = len(digits) -1
            for elem in digits[::-1]:
                if elem == 9:
                    digits[ind] = 0
                    ind = ind - 1
                else:
                    break
            if (ind+1) != 0:
                digits[ind] = digits[ind] + 1
                return digits
            else:
                return [1] + digits