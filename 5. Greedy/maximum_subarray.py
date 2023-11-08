# leetcode 53- maximum subarray
# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maximum = nums[0]
        currentSum = 0

        for n in nums:
            # reset anytime there is a negative sum
            # move l in window to new point
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maximum = max(currentSum, maximum)

        return maximum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(Solution().maxSubArray(nums))
