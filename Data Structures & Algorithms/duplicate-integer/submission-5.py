class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        """
        count = 0
        for elem in nums:
            if elem in nums[count+1:]:
                return True
            count+=1
        return False
        """