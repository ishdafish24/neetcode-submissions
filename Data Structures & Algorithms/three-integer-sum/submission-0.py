class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        for i in range(len(nums)):
            two_diff = 0 - nums[i]
            for j in range(i+1, len(nums)):
                sing_diff = two_diff - nums[j]
                if sing_diff in nums[j+1:] and ((nums[j+1:].index(sing_diff)+j+1) != j != i):
                    if sorted([nums[i], nums[j], sing_diff]) not in out:
                        out.append(sorted([nums[i], nums[j], sing_diff]))
        return out