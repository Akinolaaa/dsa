# 136- https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a = nums[0]
        for num in nums[1:]:
            a = a ^ num
        return a
