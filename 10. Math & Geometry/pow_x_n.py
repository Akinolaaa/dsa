# 50 https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(a, b):
            if(b  ==  0):
                return 1
            if a == 0:
                return 0
            res =  dfs(a, b // 2)
            res = res  * res
            
            return res if b % 2 == 0 else res * a

        sol = dfs(x, abs(n))
        return sol if n >= 0  else 1/sol