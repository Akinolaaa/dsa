# leetcode 79

class Solution:
    def __init__(self) -> None:
        pass

def word_search(grid, word):
    
    ROWS, COLS = len(grid), len(grid[0])
    def backtrack(i,j,curr):
        if (curr == word):
            return True
        if(i >= ROWS or j >= COLS or i < 0 or j < 0 or len(curr) > len(word)):
            return False
        
        curr = curr + grid[i][j]
        right = backtrack(i, j+1, curr)
        down = backtrack(i+1, j, curr)
        left = backtrack(i, j-1, curr)
        up = backtrack(i-1, j, curr)

        return right or down or left or up
    
    
    return backtrack(0,0,"")


def wordSearch(grid, word):
    ROWS, COLS = len(grid), len(grid[0])
    path = set()

    def backtrack(i,j ,pos):
        if(pos == len(word)):
            return True
        if(i >= ROWS or j >= COLS or i < 0 or j < 0 or (i,j) in path or pos >= len(word) or word[pos] != grid[i][j]):
            return False
        
        path.add((i,j))
        right = backtrack(i, j+1, pos+1)
        down = backtrack(i+1, j, pos+1)
        left = backtrack(i, j-1, pos+1)
        up = backtrack(i-1, j, pos+1)
        
        path.remove((i,j))
        return (right or down or left or up)
    
    for r in range(ROWS):
        for c in range(COLS):
            if(backtrack(r,c,0)):
                return True

    return False


r = Solution()
grid = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]]
# sol = word_search(grid, "ABCCED")
sol = wordSearch(grid, "ABCCED")
print(sol)