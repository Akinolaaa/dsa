# leetcode 695- Max area of island
import collections
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(i, j):
            count = 1
            q = collections.deque()
            q.append((i,j))
            visited.add((i,j))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while q: 
                r, c = q.pop()
                print(r, c, count)
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if(row in range(R) and col in range(C)
                        and grid[row][col] == 1 and
                        (row, col) not in visited):
                        count += 1
                        q.append((row,col))
                        visited.add((row, col))

            return count

        area = 0
        for i in range(R):
            for j in range(C):
                if(grid[i][j] == 1 and (i, j) not in visited):
                    area = dfs(i,j)
                    maxArea = max(maxArea, area)
        
        return maxArea


# 
grid = [[1,0,1],[1,0,0]]

print(Solution().maxAreaOfIsland(grid))
