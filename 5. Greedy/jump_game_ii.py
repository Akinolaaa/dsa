# leetcode 45- jump game 2

import collections


class Solution:
    # Solution similar to algorithm for minimizing a DFA
    def minimumJumps(self, nums: list[int]) -> int:
        q = collections.deque()
        q.append(0)

        jumps = 0
        while q:
            for i in range(len(q)):
                j = q.popleft()
                if j == len(nums) - 1:
                    return jumps
                if j + nums[j] <= len(nums):
                    for a in range(j + 1, j + nums[j] + 1):
                        q.append(a)
            jumps += 1

        return jumps


numbers = [2, 3, 1, 1, 4]
numbers1 = [2, 3, 0, 1, 4]

print(Solution().minimumJumps(numbers1))
