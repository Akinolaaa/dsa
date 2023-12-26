# 494-  https://leetcode.com/problems/target-sum/


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        cache = {}

        def ways(i, amount):
            if amount == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            if (i, amount) in cache:
                return cache[(i, amount)]

            cache[(i, amount)] = ways(i + 1, amount - nums[i]) + ways(
                i + 1, amount + nums[i]
            )
            return cache[(i, amount)]

        return ways(0, 0)
