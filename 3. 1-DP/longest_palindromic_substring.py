class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        maxLen = 1
        for i in range(len(s)):
            # odd numbered palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = (r + 1) - l
                if length > maxLen:
                    maxLen = length
                    longest = s[l : r + 1]
                l -= 1
                r += 1
            # even numbered
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = (r + 1) - l
                if length > maxLen:
                    maxLen = length
                    longest = s[l : r + 1]
                l -= 1
                r += 1

        return longest
