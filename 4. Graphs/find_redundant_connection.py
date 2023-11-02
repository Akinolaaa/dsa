# leetcode 684 - https://leetcode.com/problems/redundant-connection/
import collections


class Solution:
    # neetcode solution
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # solution is union find algorithm
        # n = n(edges) = n(nodes) #This will always have a cycle
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        # add union and find functions

    # my bfs solution - 4/39
    def findRedundantConnectionBFS(self, edges: list[list[int]]) -> list[int]:
        graph = {}
        visited = set()

        def bfs(n):
            q = collections.deque()
            q.append((n, 0))
            while q:
                node, exempt = q.popleft()
                for point in graph[node]:
                    if point != exempt:
                        q.append((point, node))
                    if point in visited:
                        return [node, point]
                visited.add(point)

        for a, b in edges:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]

        solution = bfs(edges[0][0])
        return solution

    # my dfs solution- 5/39
    def findRedundantConnectionDFS(self, edges: list[list[int]]) -> list[int]:
        graph = {}
        visited = set()

        def dfs(n, prev):
            if n in visited:
                return [n, prev]
            visited.add(n)
            if n in graph:
                for m in graph[n]:
                    return dfs(m, n)

        for a, b in edges:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]
            print(graph)

        solution = dfs(edges[0][0], 0)
        return solution
