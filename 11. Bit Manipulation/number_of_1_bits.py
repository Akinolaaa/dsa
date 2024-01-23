#


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:  # n > 0
            # n % 2 will return 1 if 1 is in the last position(odd number) and 0 otherwise
            res += n % 2
            n = n >> 1  # bit shift n to the right by 1
        return res

    # same time complexity but faster runtime
    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            # minus one removes the rightmost 1 bit.
            # bitwaise and turns bits to the right of rightmost to 0 and the left remains the same.
            n = n & (n - 1) 
            res += 1
        return res
