class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {i : [] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            course_map[course].append(pre_req)

        def dfs(course : int, visited : set):
            curr = course_map[course]
            if not curr:
                return True
            
            if course in visited:
                return False
            visited.add(course)
            for i in range(len(curr)-1, -1, -1):
                if not dfs(curr[i], visited):
                    return False
                curr.pop(i)
            visited.remove(course)
            return True
                
        
        for course in course_map:
            if not dfs(course, set()):
                return False
        return True