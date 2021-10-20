# https://www.lintcode.com/problem/122

# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
# find the area of largest rectangle in the histogram.


# 1. 暴力法
#    枚举区间 每个区间的矩形高度是由最小的那个高度决定的 O（N^3）
# 2. 单调栈
#    转换思维 转换到对于每个高度 其最大矩形的宽度是多少
#    对于每个高度 找到左边和右边第一个小于这个的高度的位置

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        # write your code here

        if not heights:
            return 0

        stack = []
        result = 0

        for i in range(len(heights) + 1):
            
            if i == len(heights):
                curr_height = -1
            else:
                curr_height = heights[i]
        
            while stack and heights[stack[-1]] >= curr_height:
                index = stack.pop(-1)
                height = heights[index]
                # The index of the first element on the left less than the element just popped out
                prev_index = stack[-1] if stack else -1
                # i is the index of the first element on the right less than the elemnt just popped out
                result = max(result, height * (i - prev_index - 1))
            
            stack.append(i)
        
        return result