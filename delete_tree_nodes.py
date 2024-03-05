# https://leetcode.com/problems/delete-tree-nodes/description/

# A tree rooted at node 0 is given as follows:

# The number of nodes is nodes;
# The value of the ith node is value[i];
# The parent of the ith node is parent[i].
# Remove every subtree whose sum of values of nodes is zero.
# Return the number of the remaining nodes in the tree.

class Solution(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        tree = {}
        result = [nodes]

        # {0->[1, 2], 1->[3], 2->[4, 5, 6]}
        for i in range(len(parent)):
            if parent[i] == -1:
                continue
            children = tree.get(parent[i], [])
            children.append(i)
            tree[parent[i]] = children

        def dfs(root):
            # If its a leaf node
            if root not in tree:
                if value[root] == 0:
                    # we are gonna remove it
                    result[0] -= 1
                    return (0, 0)
                else:
                    return (value[root], 1)
            
            subtree_sum = value[root]
            subtree_node = 1
            for node in tree[root]:
                sum_value, node_cnt = dfs(node)
                subtree_sum += sum_value
                subtree_node += node_cnt
            
            if subtree_sum == 0:
                result[0] -= subtree_node
                return (0, 0)
            
            return (subtree_sum, subtree_node)

        dfs(0)

        return result[0]