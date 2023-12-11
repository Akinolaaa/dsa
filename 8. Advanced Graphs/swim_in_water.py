# 778- https://leetcode.com/problems/swim-in-rising-water
import heapq


class Solution:
    # solved with dijstra's
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        minHeap = [(grid[0][0], (0, 0))]
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while minHeap:
            w, (i, j) = heapq.heappop(minHeap)
            if i == N - 1 and j == N - 1:
                return w
            for dr, dc in directions:
                a, b = i + dr, j + dc
                if a >= 0 and b >= 0 and a < N and b < N and (a, b) not in visited:
                    w1 = max(w, grid[a][b])
                    heapq.heappush(minHeap, (w1, (a, b)))
                    visited.add((a, b))
