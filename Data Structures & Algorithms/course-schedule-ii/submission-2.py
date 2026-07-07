class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = [[] for _ in range(numCourses)]
        for course, pre_req in prerequisites:
            course_map[course].append(pre_req)
        visited = [False for _ in range(numCourses)]
        result = []
        def dfs(course : int):
            curr = course_map[course]
            if visited[course]:
                return False
            if not curr:
                if course not in result:
                    result.append(course)
                return True
            visited[course] = True
            for i in range(len(curr)):
                if not dfs(curr[i]):
                    return False
            if course not in result:
                result.append(course)
            course_map[course] = []
            visited[course] = False
            return True
                        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result