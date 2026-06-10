class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        i = 0
        for elem in nums:
            if target - elem in ht:
                return [ht[target-elem], i]
            ht[elem] = i
            i+=1

            
            
        