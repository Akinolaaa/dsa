# leetcode 200- number of islands
import collections;
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        print('solving num of islands')
        numOfIslands = 0
        
        ROW, COL = len(grid), len(grid[0]);
        self.visited = set()

        def bfs(r, c):
            q = collections.deque()
            self.visted.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(ROW) and 
                        c in range(COL) and 
                        grid[r][c] == '1' and 
                        (r, c) not in self.visited):

                        self.visited.add((r, c))
                        q.append((r, c))
                    

        for r in range(ROW):
            for c in range(COL):
                if((r, c) not in self.visited and grid[r][c]=='1'):
                    bfs(r,c)
                    numOfIslands += 1
        return numOfIslands



