# 1584 - https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq


# Prims algorithm. Add kruskals later ;)
class Solution:
    def minCostConnectPoints1(self, points: list[list[int]]) -> int:
        adj = {i: [] for i in range(len(points))}

        for i in enumerate(points):
            for j in range(len(points)):
                if i == j:
                    continue
                adj[i].append(j)

        cost = 0
        visited = set()
        minHeap = []
        heapq.heappush(minHeap, [0, 0])

        def calculateDistance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        while len(visited) < len(points):
            w, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            cost += w
            for j in adj[i]:
                if j not in visited:
                    distance = calculateDistance(points[i], points[j])
                    heapq.heappush(minHeap, [distance, j])
            visited.add(i)
        return cost

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        adj = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            a, b = points[i]
            for j in range(i + 1, len(points)):
                x, y = points[j]
                distance = abs(a - x) + abs(b - y)
                adj[i].append([distance, j])
                adj[j].append([distance, i])

        cost = 0
        visited = set()
        minHeap = [[0, 0]]

        while len(visited) < len(points):
            w, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            cost += w
            visited.add(i)
            for c, point in adj[i]:
                if point not in visited:
                    heapq.heappush(minHeap, [c, point])
            print(minHeap)

        return cost


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(Solution().minCostConnectPoints(points))
