# https://leetcode.com/problems/alien-dictionary/description/

# There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

# If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

# Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = collections.defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}
        all_letters = in_degree.keys()

        max_len = max((len(word) for word in words))

        # build the graph
        # 1. Why and how we compare each pair of words
        for first_word, second_word in zip(words, words[1:]):
            for letter_1, letter_2 in zip(first_word, second_word):
                if letter_1 != letter_2:
                    if letter_2 not in graph[letter_1]:
                        graph[letter_1].add(letter_2)
                        in_degree[letter_2] +=1 
                    # why do we break here?
                    break
            else:
                # Executed if the loop completes without encountering a break statement
                # Do something else
                if len(second_word) < len(first_word):
                    return ""

        queue = collections.deque()
        visited = []
        # use items() to get all key value pairs
        for letter in all_letters:
            if in_degree[letter] == 0:
                queue.append(letter)
                visited.append(letter)
        
        # If we cannot find any letter with in degree 0, then return false
        result = ""

        while queue:
            cur = queue.popleft()
            result += cur
            for letter in graph[cur]:
                # If we found a letter which is already existed 
                if letter in visited:
                    return ""
                in_degree[letter] -= 1
                if in_degree[letter] == 0:
                    queue.append(letter)
                    visited.append(letter)
        
        return result if len(visited) == len(all_letters) else ""
        