#  198 https://leetcode.com/problems/house-robber/


class Solution:
    # my solution with better memory
    def rob(self, nums: list[int]) -> int:
        a, b = 0, 0
        # [0, 1, 2, 3, 4, n, (n + 1), a, b]
        for i in range(len(nums) - 1, -1, -1):
            t = a
            a = max(a, b + nums[i])
            b = t
        return a

    # my solution- passed all and did well
    def rob2(self, nums: list[int]) -> int:
        dp = [0] * (len(nums) + 2)
        dp[len(nums) - 1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            dp[i] = max(dp[i + 2], dp[i + 3]) + nums[i]

        return max(dp[0], dp[1])
