# leetcode 763- https://leetcode.com/problems/partition-labels/description/
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        res = []
        loc = {}
        # save last occurence of every letterr
        for i, c in enumerate(s):
            loc[c] = i
        
        # append the size to res once you reach the max
        end = total = 0
        for i, c in enumerate(s):
            end = max(loc[c], end)
            if i == end:
                res.append((end + 1) - total)
                total = i + 1
        return res


s = "ababcbacadefegdehijhklij"
sol = Solution().partitionLabels(s)
print(sol)
