# https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = collections.defaultdict(int)

        for num in nums:
            freq[num] += 1

        freq_l = [(freq, num) for num, freq in freq.items()]

        heap = []

        for item in freq_l:
            # heap always sort tuple by first element 
            # and then second and so on
            heapq.heappush(heap, item)
            if len(heap) > k:
                heapq.heappop(heap)