#  leetcode 417 - pacific atlantic flow

class Solution: 
    def pacificAtlantic(self, heights: list[list[int]] )-> list[list[int]]: 
        ROWS, COLS = len(heights), len(heights[0])
        pacificVisited, atlanticVisited = set(), set()
        res = []

        def dfs(r, c, visited, prevHeight):
            if(r < 0 or c < 0 or r>=ROWS or c>=COLS
                or (r, c) in visited or prevHeight > heights[r][c]):
                return
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacificVisited, heights[r][0])
            dfs(r, COLS - 1, atlanticVisited, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pacificVisited, heights[0][c])
            dfs(ROWS - 1, c, atlanticVisited, heig .hts[ROWS - 1][c])

        # union of both oceans
        for i in range(ROWS):
            for j in range(COLS):
                if((i,j) in pacificVisited and (i,j) in atlanticVisited):
                    res.append([i, j])

        return res
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(Solution().pacificAtlantic(heights))
