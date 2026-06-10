class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0
        e = len(nums)-1
        m = b + (e-b) // 2
        while (nums[m] != target):
            if (m == b):
                if (nums[m] == target):
                    return m
                elif (nums[e] == target):
                    return e
                else:
                    return -1
            if nums[m] < target:
                b = m
                m = b + (e-b) //2
                continue
            else:
                e = m
                m = b + (e-b)//2
                continue
        return m