# 73- https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:

    # my solution...worked fine
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        def setTo0(row, col):
            for i in range(m):
                matrix[i][col] = 0
            for i in range(n):
                matrix[row][i] = 0

        #  find 0's
        zeroes = []
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0):
                    zeroes.append((i, j))
        for r, c in zeroes:
            setTo0(r, c)