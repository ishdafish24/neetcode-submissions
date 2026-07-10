class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = list()
        m_len = 0
        c_len = 0
        for r in range(len(s)):
            if s[r] not in window:
                window.append(s[r])
                m_len = max(m_len, len(window))
            else:
                while s[r] in window:
                    window.pop(0)
                window.append(s[r])
                m_len = max(m_len, len(window))
        return m_len


        