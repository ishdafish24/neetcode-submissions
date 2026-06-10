class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        product = 1
        new_lst = []
        for elem in nums:
            if elem != 0:
                product *= elem
        if nums.count(0) >= 2:
            return [0]*len(nums)
        if nums.count(0) == 1:
            zi = nums.index(0)
            return [0]*(zi) + [product] + [0]*(len(nums)-zi-1)
        for elem in nums:
            try:
                new_lst.append(product // elem)
            except ZeroDivisionError:
                new_lst.append(product)
        return new_lst
        """
        pre = []
        prod_pre = 1
        for elem in nums:
            pre.append(prod_pre)
            prod_pre *= elem
        suf = []
        prod_suf = 1
        for elem in nums[::-1]:
            suf.append(prod_suf)
            prod_suf *= elem
        suf.reverse()
        result = []
        for i in range(len(nums)):
            result.append(pre[i] * suf[i])
        return result
