# leetcode 268- walls and gates
import collections;
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        ROW, COL = len(rooms), len(rooms[0])
        INF = 2147483647
        q = collections.deque()
        visited = set()

        def bfs(i, j, val): # bfs (i, j) changes the value of the neigbours only
            if(i < 0 or j < 0 or i >=ROW or j >=COL or 
                rooms[i][j] != INF or (i,j) in visited):
                return
            rooms[i][j] = val + 1
            q.append((i, j, val + 1))
            visited.add((i, j))

        # add gates to queue
        for i in range(ROW):
            for j in range(COL):
                if(rooms[i][j] == 0): # if room is a gate
                    q.append((i, j, 0))
                    visited.add((i, j))

        # from each gate in the bfs simultaneously
        while(q):
            stamp = len(q)
            for i in range(stamp):
                r, c, val = q.popleft()
                bfs(r + 1, c, val)
                bfs(r - 1, c, val)
                bfs(r, c - 1, val)
                bfs(r, c + 1, val)



INF = 2147483647
rooms = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF],
]
Solution().wallsAndGates(rooms)
print(rooms)



