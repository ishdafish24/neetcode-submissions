class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        for elem in nums:
            if elem in nums[count+1:]:
                return True
            count+=1
        return False