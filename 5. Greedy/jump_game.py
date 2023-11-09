#  https://leetcode.com/problems/jump-game
class Solution:
    # Theres also a DP solution but greedy is better
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0

    # 157/172 test cases passed. Failed- [2,5,0,0]
    def canJump1(self, nums: list[int]) -> bool:
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            i = i + nums[i]

        return True
