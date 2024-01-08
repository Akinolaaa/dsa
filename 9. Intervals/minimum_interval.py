import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort(key=lambda x: x[0])
        res = {}  # so we can preserve the relative order
        minHeap = []
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap, (length, intervals[i][1]))
                i += 1
            top = minHeap[0] if minHeap else [-1]
            while minHeap and q > top[1]:
                heapq.heappop(minHeap)
                top = minHeap[0] if minHeap else [-1]
            res[q] = top[0]

        return [res[q] for q in queries]


# intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
# queries = [2, 3, 4, 5]
#
intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
queries = [2, 19, 5, 22]
print(Solution().minInterval(intervals, queries))
