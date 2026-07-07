class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            course_map[crs].append(pre)

        result = []
        visit = [0 for _ in range(numCourses)] # 0 = unvisited, 1 = cycle, 2 = visited

        def dfs(course : int):
            if visit[course] == 1:
                return False
            if visit[course] == 2:
                return True

            visit[course] = 1
            for pre in course_map[course]:
                if not dfs(pre):
                    return False
            visit[course] = 2
            result.append(course)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return result