# leetcode 684 - https://leetcode.com/problems/redundant-connection/
import collections


class Solution:
    # neetcode solution- union find by rank
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # solution is union find algorithm
        # n = n(edges) = n(nodes) #This will always have a cycle
        par = [i for i in range(len(edges) + 1)] # parent- every node is initially a parent of itself till union
        rank = [1] * (len(edges) + 1) # rank is the number of nodes in the tree
        
        # find function- finding the root parent
        def find(n):
            p = par[n]
            while(p != par[n]):
                par[p] = par[par[p]] # path compression- saves time
                p = par[p]
            return p
        
        # union function
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: # redundant connection found
                return False
            
            if rank[p1] > rank[p2]: # do the union
                par[p2] = p1 # change parent
                rank[p1] += rank[p2] # increase rank of p1 cos more nodes in tree
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        res = []
        for a, b in edges:
            if(not union(a, b)):
                res = [a, b]
        return res

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
