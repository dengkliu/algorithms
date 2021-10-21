# https://www.lintcode.com/problem/126/

# Given an integer array with no duplicates. A max tree building on this array is defined as follow:
# The root is the maximum number in the array
# The left subtree and right subtree are the max trees of the subarray divided by the root number.
# Construct the max tree by the given array.
# A = [2, 5, 6, 0, 3, 1]
# {6,5,3,2,#,0,1}
# Explanation:
# the max tree constructed by this array is:
#        6
#       / \
#      5   3
#     /   / \
#    2   0   1


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# 对于每个数 是右边第一个比他大的数的左子树
# 是左边第一个比他大的数的右子树

class Solution:

    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):

        if not A:
            return None
        
        stack = []
        index_to_node = {}
        max_index = 0

        for i in range(len(A)):
            
            if A[i] > A[max_index]:
                max_index = i
            
            # 先新建一个node
            node = TreeNode(A[i])
            index_to_node[i] = node

            prev_max_node_less_than_current = None

            # 单调递减栈，前一个元素必须更大，否则弹出

            # 一直弹出，直到找到比当前元素更大的值
            # 最后一个弹出的，就是前面比当前元素小的元素里面的最大的
            # 这个最大的，要作为当前元素的左子树
            while stack and A[stack[-1]] < A[i]:
                prev_index = stack.pop(-1)
                prev_max_node_less_than_current = index_to_node[prev_index]
            if prev_max_node_less_than_current:
                node.left = prev_max_node_less_than_current    
            
            # 如果前面还有更大的元素
            # 当前元素应该成为该元素的右子树
            if stack:
                pre_index = stack[-1]
                pre_node_large_than_current = index_to_node[pre_index]
                pre_node_large_than_current.right = node
            
            stack.append(i)
        

        return index_to_node[max_index]