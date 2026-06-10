class Solution:
    def longestConsecutive(self, nums: List[int])-> int:
        nums = set(nums)
        count = 0
        for elem in nums:
            if ((elem - 1) not in nums):
                c = 1
                while ((elem + c) in nums):
                    c+=1
                if (c > count):
                    count = c
        return count