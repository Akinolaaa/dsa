# leetcode 1899: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

# Find pattern and eliminate fails
class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        candidates = set()  # [1,2,5,8]
        a = b = c = False

        for i, trip in enumerate(triplets):
            if trip[0] == target[0] or trip[1] == target[1] or trip[2] == target[2]:
                candidates.add(i)

            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                if i in candidates:
                    candidates.remove(i)

            if i in candidates:
                if trip[0] == target[0]:
                    a = True
                if trip[1] == target[1]:
                    b = True
                if trip[2] == target[2]:
                    c = True

        return a and b and c
