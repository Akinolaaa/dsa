# 268- https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res += (i - nums[i])
        res += len(nums)
        return res
    
    def missingNumber1(self, nums: list[int]) -> int:
        n = len(nums) + 1
        check = 0
        for i in range(1, n):
            check = check ^ i
        for num in nums:
            check = check ^ num
        return check
