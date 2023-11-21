#  213- https://leetcode.com/problems/house-robber-ii/description/
# algorithm is to do house robber one on two sub arrays and find the max you can rob
# subarrays - nums[:-1] and nums[1:]
class Solution:

    def rob(self, nums: list[int]) -> int:
        if(len(nums) == 1):
            return nums[0]

        # recall- [2, 3, 2, a, b]- shifting a and b to the left
        def robber(houses):
            a, b = 0, 0

            for i in range(len(houses)-1, -1, -1):
                t = a
                a = max(a, b + houses[i]) # can't rob a cos a is the next house
                b = t
            return a
        
        return max(robber(nums[:-1]), robber(nums[1:]))
