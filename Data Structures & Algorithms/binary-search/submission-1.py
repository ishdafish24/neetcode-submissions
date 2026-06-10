class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(nums, target, 0, len(nums)-1)

    def binary(self, nums: List[int], target: int, low, high):
        middle = low + (high - low) // 2
        if target == nums[middle]:
            return middle
        elif len(nums[low:high]) == 0:
            return -1
        if target > nums[middle]:
            return self.binary(nums, target, middle + 1, high)
        if target < nums[middle]:
            return self.binary(nums, target, low, middle)