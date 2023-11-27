# 300


class Solution:
    def longestIncreasingSubsequence(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        longest = 1

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    longest = max(longest, dp[i])

        return longest


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().longestIncreasingSubsequence(nums))