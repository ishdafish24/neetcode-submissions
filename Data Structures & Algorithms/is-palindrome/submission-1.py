class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for char in s:
            if char.isalnum():
                lst.append(char.lower())
        l = 0
        r = len(lst)-1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True


        
        