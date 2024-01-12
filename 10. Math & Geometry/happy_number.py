# 202- https://leetcode.com/problems/happy-number/description/


class Solution:
    # solution with Floyd's (that linkedlist algorithm for detecting cycles)
    def isHappy(self, n: int) -> bool:
        def sumOfSquaresOfDigits(a: int):
            total = 0
            while a:
                digit = a % 10
                digit = digit**2
                total += digit
                a = a // 10
            return total

        slow = sumOfSquaresOfDigits(n)
        if slow == 1:
            return True
        fast = sumOfSquaresOfDigits(sumOfSquaresOfDigits(n))
        while fast != slow:
            if slow == 1 or fast == 1:
                return True
            slow = sumOfSquaresOfDigits(slow)
            fast = sumOfSquaresOfDigits(sumOfSquaresOfDigits(fast))
        return False

    # solution without changing dtype
    def isHappy1(self, n: int) -> bool:
        def sumOfSquaresOfDigits(a: int):
            total = 0
            while a:
                digit = a % 10
                digit = digit**2
                total += digit
                a = a // 10
            return total

        sol = sumOfSquaresOfDigits(n)
        while sol != 1:
            if sol > 1 and sol < 10 and sol != 7:
                return False
            sol = sumOfSquaresOfDigits(sol)
        return True

    # my solution- idk why 7. It just works
    def isHappy2(self, n: int) -> bool:
        def sumOfSquaresOfDigits(a):
            aString = str(a)
            total = 0
            for s in aString:
                sToInt = int(s)
                total += sToInt * sToInt
            return total

        sol = sumOfSquaresOfDigits(n)
        while sol != 1:
            if sol > 1 and sol < 10 and sol != 7:
                return False
            sol = sumOfSquaresOfDigits(sol)
        return True
