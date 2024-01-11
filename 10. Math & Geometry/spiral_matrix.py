# 54-  https://leetcode.com/problems/spiral-matrix/


class Solution:
    """
    sequentially reduce the matric as you move through each edge of the spiral
    """

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        m, n = len(matrix[0]), len(matrix)
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while top < bottom and left < right:
            # move right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # move down
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            # if not (top < bottom and left < right): break # another valid case. Problem with column vectors
            if len(res) == m * n:
                break
            # move left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # move up
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
