# https://leetcode.com/problems/word-ladder/description/

# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList:
            return 0

        if endWord not in wordList:
            return 0

        queue = collections.deque()
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        step = 1

        all_combination_dict = collections.defaultdict(list)

        # Time - O(L * N)
        # This is better than 26 * L * N
        for word in wordList:
            for i in range(len(word)):
                all_combination_dict[word[:i] + '*' + word[i+1:]].append(word)

        
        def getIntermediateWord(word):
            similar_words = []
            for i in range(len(word)):
                similar_words.append(word[:i] + '*' + word[i+1:])
            return similar_words

        while queue:
            size = len(queue)
            for i in range(size):
                curr_word = queue.popleft()
                # O(L)
                intermediate_words = getIntermediateWord(curr_word)
                # worst case O(L * N * L)
                for intermediate_word in intermediate_words:
                    if intermediate_word not in visited:
                        # this word must be in the wordList
                        for word in all_combination_dict[intermediate_word]:
                            if word == endWord:
                                return step + 1
                            queue.append(word)
                        # why do we add intermediate word here to visited
                        visited.add(intermediate_word)
                        
            step += 1
            
        return 0