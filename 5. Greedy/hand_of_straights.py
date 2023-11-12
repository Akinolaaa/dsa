from collections import defaultdict
import heapq


class Solution:
    # Note: no need to save have res cos algorithm returns boolean
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if not (len(hand) % groupSize == 0):
            return False
        counts = {}
        for n in hand:
            counts[n] = 1 + counts.get(n, 0)

        heap = list(counts.keys())
        heapq.heapify(heap)
        while heap:
            print("heap--->", heap)
            smallest = heap[0]
            for i in range(smallest, smallest+groupSize):
                if i not in heap:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)

        return True


hand = [1, 2, 3, 4, 5, 6]
groupSize = 2

hand2 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize2 = 3

hand3 = [1, 1, 2, 2, 3, 3]
groupSize3 = 2

print(Solution().isNStraightHand(hand, groupSize))
