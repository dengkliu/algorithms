# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        
        # This is how we fetch all the ancestors for a target node
        parents = []
        def dfs(root, curr_nodes):
            if root.val == target.val:
                # Why do we use list() here?
                # Why are we appending this to parent, instead of just doing assigment?
                parents.append(list(curr_nodes))
                # Why do we want to return True here
                return True

            if root.left:
                curr_nodes.append(root.left)
                if dfs(root.left, curr_nodes):
                    return True
                # Why do we use backtrack here?
                curr_nodes.pop()
            if root.right:
                curr_nodes.append(root.right)
                if dfs(root.right, curr_nodes):
                    return True
                curr_nodes.pop()

        dfs(root, [root])

        queue = collections.deque()
        distance = {}
        result = []
        
        for i in range(len(parents[0])):
            target_parent = parents[0][i]
            queue.append(target_parent)
            distance[target_parent.val] = len(parents[0]) - 1 - i
            if distance[target_parent.val] == k:
                result.append(target_parent.val)

        while queue:
            node = queue.popleft()
            # Why do we want to check if the new node is in distance or not?
            if node.left and node.left.val not in distance:
                queue.append(node.left)
                distance[node.left.val] = distance[node.val] + 1
                if distance[node.left.val] == k:
                    result.append(node.left.val)
            if node.right and node.right.val not in distance:
                queue.append(node.right)
                distance[node.right.val] = distance[node.val] + 1
                if distance[node.right.val] == k:
                    result.append(node.right.val)

        return result