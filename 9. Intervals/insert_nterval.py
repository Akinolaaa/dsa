# 57- https://leetcode.com/problems/insert-interval


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        res = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            # merge and mutate newInterval
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]
        res.append(newInterval)
        return res
