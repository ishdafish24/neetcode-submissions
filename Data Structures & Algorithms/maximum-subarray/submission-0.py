class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0]
        local_sum = nums[0]
        for elem in nums[1:]:
            local_sum = max(local_sum + elem, elem)
            global_sum = max(global_sum, local_sum)
        return global_sum
        