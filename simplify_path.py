# https://leetcode.com/problems/simplify-path/

# Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.

# In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.

# The simplified canonical path should adhere to the following rules:

# It must start with a single slash '/'.
# Directories within the path should be separated by only one slash '/'.
# It should not end with a slash '/', unless it's the root directory.
# It should exclude any single or double periods used to denote current or parent directories.
# Return the new path.


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        index = 0
        stack = []

        while index < len(path):
            letter = path[index]
            if letter == '/':
                if stack and stack[-1] == '/':
                    index += 1
                else:
                    stack.append(letter)
                    index += 1
            elif letter == '.':
                dot_cnt = 1
                index += 1
                while index < len(path) and path[index] == '.':
                    dot_cnt += 1
                    index += 1
                
                # 1. check if it's only dots between dashes
                if stack[-1] != '/' or (index < len(path) and path[index] != '/'):
                    for i in range(dot_cnt):
                        stack.append('.')
                    continue
                # 2. current directory
                elif dot_cnt == 1:
                    # 2.1 root directory
                    if len(stack) == 1:
                        continue
                    # 2.2 remove previous /
                    else:
                        stack.pop()
                # 3. previous directory
                elif dot_cnt == 2:
                    # 3.1 root directory
                    if len(stack) == 1:
                        continue
                    # 3.2 remove previous / and previous directory name
                    else:
                        stack.pop()
                        while stack and stack[-1] != '/':
                            stack.pop()
                else:
                    for i in range(dot_cnt):
                        stack.append('.')
            else:
                stack.append(letter)
                index += 1

        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()

        return ''.join(stack)