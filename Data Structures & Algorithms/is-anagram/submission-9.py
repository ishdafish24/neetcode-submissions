class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht_s = {}
        ht_t = {}
        for char in s:
            if char not in ht_s:
                ht_s[char] = 1
            else:
                ht_s[char] += 1
        for char in t:
            if char not in ht_t:
                ht_t[char] = 1
            else:
                ht_t[char] += 1
        return ht_s == ht_t        