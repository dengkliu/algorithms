# https://leetcode.com/problems/maximum-swap/

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 2736
        # 2 -> {0}
        # 7 -> {1}
        # 3 -> {2}
        # 6 -> {3}

        s = str(num)
        c_indexes = collections.defaultdict(int)

        for i, c in enumerate(s):
            c_indexes[int(c)] = i

        for i, c in enumerate(s):
            n = int(c)
            for m in range(9, n, -1):
                if c_indexes[m] > i:
                    index = c_indexes[m]
                    return int(s[0:i] + str(m) + s[i + 1:index] + str(n) + s[index + 1:])

        return int(s)