# Leetcode 78
#     .
#   /   \
# [1]    []  

class Solution: 
    
  def subsets(self, nums: list[int]) -> list[list[int]]:
    res = [];
    subset = []

    def dfs(i):
      if (i >= len(nums)):
        res.append(subset[:]) #subset.copy()
        return
      
      # add a number to subset
      subset.append(nums[i]);
      dfs(i+1);

      # add an empty array to subset
      subset.pop()
      dfs(i+1);
    
    dfs(0);
    return res;

solution = Solution()
print(solution.subsets([1,2,3]))  
