# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dictt = {}

        for pair in prerequisites:
            i, j = pair
            dictt[i] = j
            if(j in dictt):
                return False
        return True



    # first solution. Only passed 42/52 test cases
    #  failed:
    # 5,  [[1,4],[2,4],[3,1],[3,2]]
    def canFinish1(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        dictt = {}

        for pair in prerequisites:
            i, j = pair
            dictt[i] = j
            if(j in dictt):
                return False
        return True
        