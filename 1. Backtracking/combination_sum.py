# leetcode 39

class Solution:
    
    def subsets(self, candidates: list[int], target: int) -> list[list[int]]:
      res = []

      def dfs(i, possible_sums, total):
        if(total == target):
          res.append(possible_sums.copy());
          return
        
        if(total > target or i >= len(candidates)):
          return
        
        possible_sums.append(candidates[i])
        dfs(i, possible_sums, total+candidates[i]);
        possible_sums.pop()
        dfs(i + 1, possible_sums, total)
      
      dfs(0,[],0);
      return res;

r = Solution()
print(r.subsets([2,3,6,7],7))
        

          