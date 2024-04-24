# https://leetcode.com/problems/validate-binary-tree-nodes/

# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

# Note that the nodes have no values and that we only use the node numbers in this problem.

# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false


class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        in_degree = [0] * n

        for i in range(n):
            if leftChild[i] != -1:
                in_degree[leftChild[i]] += 1
                # one node shouldn't have more than one parent
                if in_degree[leftChild[i]] > 1:
                    return False
            if rightChild[i] != -1:
                in_degree[rightChild[i]] +=1
                # one node shouldn't have more than one parent
                if in_degree[rightChild[i]] > 1:
                    return False

        root = []

        for i in range(n):
            if in_degree[i] == 0:
                root.append(i)
        
        # there should just be one root
        if len(root) != 1:
            return False
        
        queue = collections.deque()
        queue.append(root[0])
        visited = set()
        visited.add(root[0])

        while queue:
            curr = queue.popleft()
            l = leftChild[curr]
            r = rightChild[curr]
            if l != -1:
                # if l in visited:
                #    return False
                in_degree[l] -= 1
                if in_degree[l] == 0:
                    queue.append(l)
                    visited.add(l)

            if r != -1:
                # if r in visited:
                #    return False
                in_degree[r] -= 1
                if in_degree[r] == 0:
                    queue.append(r)
                    visited.add(r)

        return len(visited) == n