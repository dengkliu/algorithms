# https://leetcode.com/problems/network-delay-time/

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])

        queue = collections.deque()
        queue.append(k)
        distance = [float('inf') for i in range(n + 1)]
        distance[k] = 0
        result = 0

        while queue:
            cur = queue.popleft()
            for child, w in graph[cur]:
                # Why do we want to compare the distance
                if distance[cur] + w < distance[child]:
                    distance[child] = distance[cur] + w
                    queue.append(child)

        result = float('-inf')
        for i in range(1, n + 1):
            if distance[i] == float('inf'):
                return -1
            result = max(result, distance[i])
                            
        return result