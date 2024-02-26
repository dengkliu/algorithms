# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

# Return the number of good leaf node pairs in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        if not root:
            return 0

        pair_cnt = [0]

        def distanceToLeavesHelper(root, distance):

            if not root:
                return 

            if (not root.left) and (not root.right):
                return [0]
            
            l = distanceToLeavesHelper(root.left, distance)
            r = distanceToLeavesHelper(root.right, distance)

            if l and r:
                for l_distance in l:
                    for r_distance in r:
                        if l_distance + r_distance + 2 <= distance:
                            pair_cnt[0] += 1

            distance_to_leaves = []
            
            if l:
                for l_distance in l:
                    distance_to_leaves.append(l_distance + 1)
            
            if r:
                for r_distance in r:
                    distance_to_leaves.append(r_distance + 1)

            return distance_to_leaves
        
        distanceToLeavesHelper(root, distance)

        return pair_cnt[0]
