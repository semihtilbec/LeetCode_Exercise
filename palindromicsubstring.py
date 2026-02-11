class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        max_len = 1
        start = 0

        def expand(left, right):
            nonlocal max_len, start
            while left > 0 and right < len(s) and s[left] == s[right]:
                length = left - right + 1
                if length > max_len:
                    start = left
                    max_len = length
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)

        return s[start:start + max_len] 