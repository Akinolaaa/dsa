

class Solution: 
  def solution(self, interval, processes):
    res = []
    instances = [k for k in range(processes)]

    def dfs(i, curr):
      if (len(curr) > interval or i >= len(instances)):
        return;
    
      if (len(curr) == interval and curr not in res):
        res.append(curr[:])
    
      curr.append(instances[i]);
      dfs(i, curr); 
      curr.pop();
      dfs(i+1, curr)

    dfs(0,[])
    return res

r = Solution()
print(r.solution(3,4))

