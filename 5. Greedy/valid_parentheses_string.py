# leetcode 678- https://leetcode.com/problems/valid-parenthesis-string/description/
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax = leftMin = 0
        for c in s:
            if c == "(":
                leftMax += 1
                leftMin += 1
            elif c == ")":
                leftMax -= 1
                leftMin = max(0, leftMin - 1)
            else:
                leftMax += 1
                leftMin = max(0, leftMin - 1)
            if leftMax < 0:
                return False
        return leftMin == 0

    # failed- solved 40/67 test cases
    def checkValidString1(self, s: str) -> bool:
        if s[0] == ")":
            return False
        counter = 0
        asteriskCount = 0

        for c in s:
            if c == "(":
                counter += 1
            elif c == ")":
                counter -= 1
            else:
                asteriskCount += 1

        for _ in range(asteriskCount):
            if counter == 0:
                break
            if counter > 0:
                counter -= 1
            if counter < 0:
                return False

        return counter == 0
