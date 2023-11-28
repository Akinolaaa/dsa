#  332 -https://leetcode.com/problems/reconstruct-itinerary/
import collections


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # construct adjacency list
        graph = collections.defaultdict(lambda: [])

        tickets.sort()  # sorts by first item then second if first is equal instead of sorting each list
        for f, t in tickets:
            graph[f].append(t)

        # for port in graph.keys():
        #     graph[port].sort()
        ans = []
        def helper(node):
            while graph[node]:
                helper(graph[node].pop(0))

            ans.append(node)

        helper("JFK")
        return reversed(ans)

    def findItinerary1(self, tickets: list[list[str]]) -> list[str]:
        # construct grapgacency list
        graph = collections.defaultdict(lambda: [])

        tickets.sort()  # sorts by first item then second if first is equal instead of sorting each list
        for f, t in tickets:
            graph[f].append(t)

        # for port in graph.keys():
        #     graph[port].sort()

        res = ["JFK"]

        def dfs(port):
            if len(res) == len(tickets) + 1:  # this means we have traversed every node
                return True
            if (
                port not in graph
            ):  # this means it  has no outgoing edges and we get stuck
                return False

            temp = list(graph[port])  # getting storing this so we can mutate it
            for i, dest in enumerate(temp):
                graph[port].pop(i)  # assume this edge is a viable solution
                res.append(dest)  # add to res
                if dfs(dest):  # if viable
                    return True
                # else put it back in the list and remove it(like backtracking)
                graph[port].insert(i, dest)
                res.pop()
            return False

        dfs("JFK")
        return res
