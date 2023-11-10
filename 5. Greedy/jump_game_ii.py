# leetcode 45- jump game 2

import collections
# Solution similar to algorithm for minimizing a DFA
class Solution:
    # neetcode solution
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res



    def minimumJumps(self, nums: list[int]) -> int:
        q = collections.deque()
        q.append(0)
        visited = set()
        jumps = 0
        while q:
            for i in range(len(q)):
                j = q.popleft()
                if j == len(nums) - 1:
                    return jumps
                for a in range(j + 1, j + nums[j] + 1):
                    if a not in visited and a < len(nums):
                        q.append(a)
                        visited.add(a)
                    # early return
                    if a == len(nums) - 1:
                        return jumps + 1
            jumps += 1

        return jumps


numbers = [2, 3, 1, 1, 4]
numbers1 = [2, 3, 0, 1, 4]
numbers2 = [3, 4, 3, 2, 5, 4, 3]
numbers3 = [9, 8, 2, 2, 0, 2, 2, 0, 4, 1, 5, 7, 9, 6, 6, 0, 6, 5, 0, 5]

print(Solution().minimumJumps(numbers3))
print(Solution().jump(numbers3))
