# leetcode 261-  Graph valid tree
# Lintkcode 178
# Given a list of undirected edges, check whether the graph is a valid tree
""" 
Returns false if disjoint or if cycle
"""


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # initalize adjacency list
        graph = {i: [] for i in range(n)}

        # fill up adjacency list
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        def dfs(node, prev):
            for n in graph[node]:
                if n not in visited and n != prev:
                    dfs(n, node)
            visited.add(node)

        # do a dfs on any node
        dfs(edges[0][0], -1)
        for i in range(n):
            if i not in visited:
                return False

        return True


connects = [[0, 1], [0, 2], [0, 3], [1, 4]]
connects2 = [[0, 1], [0, 2], [0, 3], [1, 4], [5, 6]]
print(Solution().validTree(7, connects2))
