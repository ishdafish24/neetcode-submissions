class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        iteration = 0
        l = 0
        r = len(heights)-1
        while l < r:
            iteration = (r-l)*min(heights[l], heights[r])
            ans = max(ans, iteration)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return ans