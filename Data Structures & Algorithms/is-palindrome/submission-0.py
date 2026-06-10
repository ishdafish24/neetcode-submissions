class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = list(s)
        stripped = []
        for char in s:
            if char.isalnum():
                stripped.append(char)
        return stripped == stripped[::-1]
        