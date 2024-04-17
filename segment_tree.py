class SegmentTreeNode:
    def __init__(self, start, end, sum=0):
        self.start = start
        self.end = end
        self.sum = sum
        self.l = None
        self.r = None
    
class SegmentTree:
    def build_segment_tree(self, input_array, start, end):
        if start == end:
            return SegmentTreeNode(start, end, input_array[start])
        
        mid = (start + end)//2
        l = self.build_segment_tree(input_array, start, mid)
        r = self.build_segment_tree(input_array, mid + 1, mid)

        node = SegmentTreeNode(start, end, left_child.range_sum + right_child.range_sum)
        node.l = l
        node.r = r
        return node

    def range_sum_query(self, node, query_start, query_end):
        if query_start == node.start and query_end == node.end:
            return node.range_sum
        
        mid = (node.start + node.end)//2

        if query_end <= mid:
            return self.range_sum_query(node.l, query_start, query_end)
        elif query_start > mid:
            return self.range_sum_query(node.r, query_start, query_end)
        else:
            return self.range_sum_query(node.l, query_satrt, mid) + range_sum_query(node.r, mid + 1, query_end)
    
    def modify(self, node, index, value):
        if node.start == node.end == index:
            node.sum = value
        
        mid = (node.start + node.end)//2
        if index <= mid:
            self.modify(node.l, index, value)
        else:
            self.modify(node.r, index, value)
        
        node.sum = node.l.sum + node.r.sum

class Solution:
    def countSmaller(self, nums):
        # because values can be negative, we add an offset to transform them to postive
        offset = 10**4
        size = 2 * 10**4 + 1 # total possible values in nums plus one dummy
        array = [0] * size
        segment_tree = SegmentTree()
        tree = segment_tree.build_segment_tree(array, 0, size - 1)

        result = []
        for num in reversed(nums):
            smaller_count = SegmentTree.range_sum_query(tree, 0, num + offset - 1)
            result.append(smaller_count)
            SegmentTree.modify(tree, num + offset - 1, 1)
        
        return result


