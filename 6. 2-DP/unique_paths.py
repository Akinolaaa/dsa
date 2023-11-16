# leetcode 62-https://leetcode.com/problems/unique-paths/description/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [
            [0 for _ in range(n + 1)] for i in range(m + 1)
        ]  # extra layer for index-out-of-bounds problem
        dp[m - 1][n - 2] = 1
        dp[m - 2][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if dp[i][j] != 0:
                    continue
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

    # neetcode algorithm. Essentially the same but it saves time
    def uniquePaths1(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
                row = newRow

            return row[0]


sol = Solution().uniquePaths(1, 1)
print(sol)
