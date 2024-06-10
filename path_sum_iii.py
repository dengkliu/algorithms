# https://leetcode.com/problems/path-sum-iii/

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        def pre_order(root, cur_sum):
            nonlocal total_cnt
            if not root:
                return

            cur_sum += root.val

            if cur_sum - targetSum in sum_to_cnt:
                total_cnt +=  sum_to_cnt[cur_sum - targetSum]
            
            sum_to_cnt[cur_sum] += 1
            pre_order(root.left, cur_sum)
            pre_order(root.right, cur_sum)
            # Remove the current sum from the hashmap
            # in order not to use it during 
            # the parallel subtree processing
            sum_to_cnt[cur_sum] -= 1

        total_cnt = 0 
        sum_to_cnt = collections.defaultdict(int)
        sum_to_cnt[0] = 1
        pre_order(root, 0)
        return total_cnt
        