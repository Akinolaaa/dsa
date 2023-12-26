# 97- https://leetcode.com/problems/interleaving-string/description/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        cache = {}

        def backtrack(a, b):
            if a == len(s1) and b == len(s2):
                return True
            if (a, b) in cache:
                return cache[(a, b)]
            if a < len(s1) and s1[a] == s3[a + b] and backtrack(a + 1, b):
                cache[(a, b)] = True
                return True
            if b < len(s2) and s2[b] == s3[a + b] and backtrack(a, b + 1):
                cache[(a, b)] = True
                return True

            cache[(a, b)] = False
            return False

        return backtrack(0, 0)
