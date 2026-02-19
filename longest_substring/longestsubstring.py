class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            letters = set()
            left = 0
            max_substring = 0
            for right in range(len(s)):
                while s[right] in letters:
                    letters.remove(s[left])
                    left += 1
                
                letters.add(s[right])
                max_substring = max(max_substring, right - left + 1)
            return max_substring
sentence = input("Enter the sentence: ")
solution = Solution()
result = solution.lengthOfLongestSubstring(sentence)
print(result)
        