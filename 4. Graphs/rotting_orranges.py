# 994 - rotting oranges
#  https://leetcode.com/problems/rotting-oranges/
import collections
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = collections.deque()
        minutes, fresh = 0, 0

        # initialize q with all 2's
        for r in range(ROW):
            for c in range(COL):
                if(grid[r][c] == 2):
                    q.append((r, c, 0))
                if(grid[r][c] == 1):
                    fresh += 1

        while(q):
            i, j, minute = q.popleft()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                r , c = i + dr, j + dc
                if(r >=0 and c >= 0 and r < ROW and c < COL and grid[r][c] == 1):
                    fresh -= 1
                    grid[r][c] = 2
                    q.append((r, c, minute + 1))
            minutes = minute

        if(fresh > 0):
            return -1
        return minutes

grid1 = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
grid3 = [[0,2]]
print(Solution().orangesRotting(grid1))