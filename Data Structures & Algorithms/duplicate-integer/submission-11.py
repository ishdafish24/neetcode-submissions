class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = set()
        for elem in nums:
            if elem in ht:
                return True
            ht.add(elem)
        return False
        