# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        hashMap = { i:[] for i in range(numCourses)} # initalize each course with an empty list

        for crs, pre in prerequisites:
            hashMap[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if hashMap == []:
                return True
            
            visited.add(crs)
            for pre in hashMap[crs]:
                if not dfs(pre):
                    return False
                visited.remove(crs)
                hashMap[crs] = []
                return True
        
        for course in range(numCourses):
            if not dfs(course):
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
        
print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))