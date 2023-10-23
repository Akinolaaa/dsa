# leetcode 40
# same as combination sum with no duplicates
# [1,1,2,5,6,7,10]
class Solution:

    def combination_sum(self, nums:list[int], target:int)->list[list[int]]:
        res = []
        nums.sort()

        def dfs(i, arr, total):
            if (total == target):
                res.append(arr[:]);
                return;
            if(total > target or i >= len(nums)):
                return;

            # left side- add a number that will give a possibe sum
            arr.append(nums[i]);
            dfs(i+1, arr, total + nums[i])
            while( i+1 < len(nums) and nums[i] == nums[i+1]):
                i += 1

            # right side- add empty
            arr.pop()
            dfs(i + 1, arr, total)

        dfs(0, [], 0)
        return res;

    def neet_combination_sum(self, nums:list[int], target:int)->list[list[int]]:
        nums.sort()
        res = []

        def backtrack(pos, cur, target):
            if target == 0:
                res.append(cur[:])
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(nums)):
                if nums[i] == prev:
                    continue;
                cur.append(nums[i])
                backtrack(i+1, cur, target-nums[i])
                cur.pop()
                prev = nums[i]

        backtrack(0, [], target)
        return res;


r =  Solution()
# print(r.neet_combination_sum([10,1,2,7,6,1,5],8))
print(r.combination_sum([10,1,2,7,6,1,5],8))