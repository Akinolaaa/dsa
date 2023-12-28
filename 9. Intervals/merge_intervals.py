# 56- https://leetcode.com/problems/merge-intervals/


class Solution:
    # my solution correctttt- O(nlogn) cos of sort
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()  # intervals.sort(key=lambda i: i[0])
        res = []
        i = 0
        while i < len(intervals) - 1:
            if intervals[i + 1][0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                intervals[i + 1] = [
                    min(intervals[i + 1][0], intervals[i][0]),
                    max(intervals[i + 1][1], intervals[i][1]),
                ]
            i += 1
        res.append(intervals[-1])
        return res

    # neetcode solution- O(nlogn) cos of sort
    def merge2(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
