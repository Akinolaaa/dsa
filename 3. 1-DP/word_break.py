# leetcode 139- word_break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = [False] * len(s)

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                end = i + len(word)
                if(end > len(s)):
                    continue
                if(s[i:end] == word):
                    print(s[i:end])
                    dp[i] = dp[end]
                if(dp[i]):
                    break

        return dp[0]



solulu = Solution()
solve = solulu.wordBreak("catsandog", ["cats","dog","sand","and","cat"])

print(solve);