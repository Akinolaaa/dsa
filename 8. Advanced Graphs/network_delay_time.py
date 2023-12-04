# 743  https://leetcode.com/problems/network-delay-time/
import heapq
class Solution:
    #  better space
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}

        for u,v,w in times:
            adj[u].append((v, w))

        visited = set()
        minHeap =  [(0, k)]
        maxim = 0
        while len(visited) < n:
            if not minHeap:
                return -1
            w, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            maxim = w
            for v, cost in adj[node]:
                if v in visited:
                    continue
                totCost = w + cost
                heapq.heappush(minHeap,(totCost, v))
            visited.add(node)
            
        return maxim
    
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            adj[u].append((v, w))

        visited = set()
        minHeap = [(0, k)]
        nodeCostFrmSrc = [100000] * (n + 1)
        nodeCostFrmSrc[k] = 0
        while len(visited) < n:
            if not minHeap:
                return -1
            w, node = heapq.heappop(minHeap)
            for v, cost in adj[node]:
                if v in visited:
                    continue
                totCost = w + cost
                if totCost < nodeCostFrmSrc[v]:
                    heapq.heappush(minHeap, (totCost, v))
                    nodeCostFrmSrc[v] = totCost

            visited.add(node)

        return max(nodeCostFrmSrc[1:])


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))

# [[1,2,1],[2,1,3]] n = 2, k = 2
