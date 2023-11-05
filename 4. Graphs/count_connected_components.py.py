# leetcode 323- Number of connected components in an undirected graph
# A leetcode premium problem
class Solution:
    # My Algorithm
    """
    Perform union find on edge with rank
    Return number of distinct parents in parents array
    Neetcode- A better way is to return 1 if there's a union and 0 if there isn't and subtract from the number of nodes
    Another solution is to draw the graph and perform dfs on every node not seen
    """

    def func(self, numNodes: int, edges: list[list[int]]) -> int:
        par = [i for i in range(numNodes)]
        rank = [1] * numNodes

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return p1

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                return p1
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
                return p2

        distinct_parents = set()
        for a, b in edges:
            s = union(a, b)
            print(s)
            distinct_parents.add(s)

        return len(distinct_parents)


print(Solution().func(5, [[0, 1], [1, 2], [3, 4]]))
