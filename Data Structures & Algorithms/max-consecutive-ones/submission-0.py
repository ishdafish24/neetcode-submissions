class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        c = 0
        for elem in nums:
            if elem == 1:
                c += 1
                if c > count:
                    count = c
                continue
            else:
                c = 0
        return count