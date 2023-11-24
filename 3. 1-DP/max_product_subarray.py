# 152 - https://leetcode.com/problems/maximum-product-subarray/

""" 
Solution Explanation.
-ve integergers are the problem with this question cos product of negative integers causes the sign toalternate as each product is done. From this pattern a dp solution is formed.
Summary. Because it is possible for the current minimum value to be multiplied by n to give the new maximum product. It is important for it to be stored too.
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                # cos it will kill the  product so it's best to start over
                curMin, curMax = 1, 1
                continue
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)
