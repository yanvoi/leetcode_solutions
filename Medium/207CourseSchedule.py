class Course:
    
    def __init__(self):
        self.makes_course_available = []
        # visited_status == -1 means it's being visited right now
        # visited_status == 1 means it's been visited without finding a cycle
        # visited_status == 0 means it hasn't been visited yet
        self.visited_status = 0

        
class Graph:
    
    def __init__(self, n):
        self.courses = [Course() for _ in range(n)]
        
    def add_correlation(self, obj, pre):
        self.courses[pre].makes_course_available.append(obj)
        
    def check_if_cycle_exists(self, course):
        
        if self.courses[course].visited_status == 1:
            return False
        
        if self.courses[course].visited_status == -1:
            return True
        
        self.courses[course].visited_status = -1
        
        for objective in self.courses[course].makes_course_available:
            if self.check_if_cycle_exists(objective):
                return True
            
        self.courses[course].visited_status = 1
        return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = Graph(numCourses)
        for objective, prerequisite in prerequisites:
            graph.add_correlation(objective, prerequisite)
            
        for num in range(numCourses):
            if graph.check_if_cycle_exists(num):
                return False
            
        return True
        
