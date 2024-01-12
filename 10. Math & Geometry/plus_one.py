#   66-  https://leetcode.com/problems/plus-one/description/


class Solution:
    # my solution- works fine. Passes all test cases
    def plusOne(self, digits: list[int]) -> list[int]:
        sol = digits[::-1]
        a = 0
        carry = 1
        while carry > 0:
            num = sol[a] + carry
            carry = num // 10
            sol[a] = num % 10
            a += 1
            if a == len(sol) and carry > 0:
                sol.append(0)
        return sol[::-1]
