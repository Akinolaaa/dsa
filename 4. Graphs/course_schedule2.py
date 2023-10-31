class Solution:

    # failed- passed 32/45 test cases
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = set()
        node = {}
        visited = set()
        # create graph with adjacency list
        def dfs(crs):
            if(node[crs] == []):
                res.add(crs)
                return True
            if(crs in visited):
                return False
            visited.add(crs)
            for c in node[crs]:
                if(not dfs(c)):
                    return False
                visited.remove(crs)
                node[crs] = []
                res.add(crs)
                return True

        for c in range(numCourses):
            node[c] = []
        
        for crs, pre in prerequisites:
            node[crs].append(pre)

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return list(res)

        