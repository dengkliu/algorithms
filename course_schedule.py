# https://www.lintcode.com/problem/615/
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Before taking some courses, you need to take other courses. 
# For example, to learn course 0, you need to learn course 1 first, which is expressed as [0,1].
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Input: n = 2, prerequisites = [[1,0]] 
# Output: true

# 典型的拓扑排序问题 要验证有向无环图

class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses, prerequisites):

        course_to_indegrees = {i:0 for i in range(num_courses)}
        course_to_courses = {i:[] for i in range(num_courses)}

        for prerequisite in prerequisites:
            course_to_courses[prerequisite[1]].append(prerequisite[0])
            course_to_indegrees[prerequisite[0]] +=1

        start_courses = [course for course in course_to_indegrees if course_to_indegrees[course] == 0]
        queue = collections.deque(start_courses)
        courses = []

        while queue:
            current_course = queue.popleft()
            courses.append(current_course)

            for next_course in course_to_courses[current_course]:
                course_to_indegrees[next_course] -= 1
                if course_to_indegrees[next_course] == 0:
                    queue.append(next_course)

        
        if len(courses) == num_courses:
            return True
        
        return False