class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = [[] for _ in range(numCourses)]
        for course, pre_req in prerequisites:
            course_map[course].append(pre_req)
        visited = [False for _ in range(numCourses)]

        def dfs(course : int):
            curr = course_map[course]
            if visited[course]:
                return False
            if not curr:
                return True
            visited[course] = True
            for i in range(len(curr)):
                if not dfs(curr[i]):
                    return False
            course_map[course] = []
            visited[course] = False
            return True
                        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True