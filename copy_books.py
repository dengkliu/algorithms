# https://www.lintcode.com/problem/437/
# Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.
# These books list in a row and each person can claim a continous range of books. 
# For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).
# They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. 
# What's the best strategy to assign books so that the slowest copier can finish at earliest time?
# Return the shortest time that the slowest copier spends.

# Input: pages = [3, 2, 4], k = 2
# Output: 5
# Explanation:
#    First person spends 5 minutes to copy book 1 and book 2.
#    Second person spends 4 minutes to copy book 3.

# 1. Brute force. 枚举所有的分组情况，然后比较需要的最短时间，打擂台。时间复杂度 C(N, K) -- 把N个数分成K组
# 2. 在解空间里进行二分。
#    最短的时间是多少？--> 当我们有足够的人，可以一人分一个书，那么最慢的那个人话的时间就是书籍页数的最大值
#    最长的时间是多少？--> 当我们只有一个人，必须完成所有书，那么最慢的时间是全部书籍页数的和
#    对于每个时间，我们只需要check，当我们规定每个人不超过这个时间，那么我们需要多少人，< K? 我们能继续降低limit >K? 我们完成不了，只能增加limit

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0

        # 确定答案范围
        total_pages = self.__get_total_pages(pages)
        start, end = 0, total_pages
        
        while start + 1 < end:
            mid = (start + end)//2
            if self.__can_finish(mid, pages, k):
                end = mid
            else:
                start = mid
        
        if self.__can_finish(start, pages, k):
            return start
        else:
            return end
    
    def __get_total_pages(self, pages):
        total_pages = 0
        for page in pages:
            total_pages += page
        return total_pages
    
    def __can_finish(self, page_limit, pages, k):
        worker_cnt = 1
        pages_cnt = 0
        for page in pages:
            if page > page_limit:
                return False
            if pages_cnt + page <= page_limit:
                pages_cnt += page
            else:
                worker_cnt += 1
                pages_cnt = page
                if worker_cnt > k:
                    return False
        
        return True