class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for ind, elem in enumerate(nums):
            for ind1, elem1 in enumerate(nums[ind+1:]):
                if elem == elem1:
                    return True
        return False