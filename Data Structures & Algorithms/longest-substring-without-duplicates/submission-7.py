class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        rp = 0
        max_len = 0
        window = set()
        for elem in s:
            if elem not in window:
                window.add(elem)
                rp += 1
                max_len = max(max_len, rp-lp)
            else:
                while elem in window:
                    window.remove(s[lp])
                    lp += 1
                window.add(elem)
                rp += 1
        return max_len




        