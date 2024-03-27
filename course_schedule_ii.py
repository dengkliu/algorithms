# https://leetcode.com/problems/course-schedule-ii/description/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an
# array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want # to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return # any of them. If it is impossible to finish all courses, return an empty array.


class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def findOrder(self, num_courses, prerequisites):

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
            return courses
        
        return []