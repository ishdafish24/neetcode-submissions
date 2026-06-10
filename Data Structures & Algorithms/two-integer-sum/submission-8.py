class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for elem in nums:
            diff = target - elem
            if diff in nums:
                ind_diff = len(nums)-1 - nums[::-1].index(diff)
                if nums.index(elem) != ind_diff:
                    return [nums.index(elem), ind_diff]