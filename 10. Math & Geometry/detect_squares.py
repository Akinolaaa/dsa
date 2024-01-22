#  2013- https://leetcode.com/problems/detect-squares/
from collections import defaultdict;

class DetectSquares:

    def __init__(self):
        self.pointsMap = defaultdict(int)
        self.lis = []

    def add(self, point: list[int]) -> None:
        self.pointsMap[tuple(point)] += 1
        self.lis.append(tuple(point))

    def count(self, point: list[int]) -> int:
        res = 0
        Px, Py = point
        for x, y in self.lis:
            if abs(Px - x) != abs(Py - y) or Px == x or Py == y:
                continue
            res += self.pointsMap[(Px, y)] * self.pointsMap[(x, Py)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)