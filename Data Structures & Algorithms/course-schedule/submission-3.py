class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {i : [] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            course_map[course].append(pre_req)
        visited = set()
        def dfs(course : int):
            curr = course_map[course]

            if course in visited:
                return False
            if not curr:
                return True
            
            visited.add(course)
            for i in range(len(curr)-1, -1, -1):
                if not dfs(curr[i]):
                    return False
                curr.pop(i)
            visited.remove(course)
            return True
                
        
        for course in course_map:
            if not dfs(course):
                return False
        return True