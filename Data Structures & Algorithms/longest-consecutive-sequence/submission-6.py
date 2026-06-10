class Solution:
    def longestConsecutive(self, nums: List[int])-> int:
        max_count = 0
        for elem in list(set(nums)):
                count = 1
                c = 1
                while elem+c in list(set(nums)):
                    count += 1
                    c += 1
                if count > max_count:
                    max_count = count
                count = 0
        return max_count