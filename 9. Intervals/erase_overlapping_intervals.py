# 435- https://leetcode.com/problems/non-overlapping-intervals/description/


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        for i in range(0, len(intervals) - 1):
            if intervals[i + 1][0] < intervals[i][1]:
                res += 1
                if intervals[i + 1][1] > intervals[i][1]:
                    intervals[i + 1] = [intervals[i][0], intervals[i][1]]
                #  basically delete the one with the longer length- the longer is more likely to overlap with others
                # i + 1 remains the same if it is the shorter interval
        return res

        # other solution
        intervals.sort(key=lambda x: x[0])
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:] :
            if start >= end:
                prevEnd = end
            else: 
                res += 1
                prevEnd = min(prevEnd, end)
