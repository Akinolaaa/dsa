class Solution: 
    # sort so the i can increase if it sees a number it's seen before to avoid repetition
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [];
        subset = []

        def dfs(i):
            if (i >= len(nums) and subset not in res):
                res.append(subset[:]) #subset.copy()
                return
            if (i >= len(nums)):
                return
            # add a number to subset
            subset.append(nums[i]);
            dfs(i+1);

            # add empty array to subset
            subset.pop()
            dfs(i+1);
            
        dfs(0);
        return res;

solution = Solution()
print(solution.subsets([1,2,2,3]))  
