# https://www.lintcode.com/problem/805/

# Amazon sells books, every book has books which are strongly associated with it. 
# Given ListA and ListB,indicates that ListA [i] is associated with ListB [i] which represents the book and associated books. 
# Output the largest set associated with each other(output in any sort). 
# You can assume that there is only one of the largest set.

# The number of books does not exceed 5000.

# Example 1:
#	Input:  ListA = ["abc","abc","abc"], ListB = ["bcd","acd","def"]
#	Output:  ["abc","acd","bcd","def"]
#	Explanation:
#	abc is associated with bcd, acd, dfe, so the largest set is the set of all books
	
# Example 2:
#	Input:  ListA = ["a","b","d","e","f"], ListB = ["b","c","e","g","g"]
#	Output:  ["d","e","f","g"]
#	Explanation:
#	The current set are [a, b, c] and [d, e, g, f], then the largest set is [d, e, g, f]

class UnionFind:

    def __init__(self):
        self.father = {}
        self.size_of_set = {}
        self.element_of_set = {}
    
    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.size_of_set[x] = 1
        self.element_of_set[x] = [x]
    
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        self.father[root_x] = root_y
        self.size_of_set[root_y] += self.size_of_set[root_x]
        self.element_of_set[root_y] += self.element_of_set[root_x]

        del self.size_of_set[root_x]
        del self.element_of_set[root_x]


class Solution:

    def __init__(self):
        self.uf = UnionFind()

    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        
        if not ListA or not ListB:
            return []
        
        if len(ListA) != len(ListB):
            return []

        n = len(ListA)

        for i in range(n):
            self.uf.add(ListA[i])
            self.uf.add(ListB[i])
            self.uf.merge(ListA[i], ListB[i])

        max_set_size = 0
        max_set_key = ""
        
        for key, value in self.uf.size_of_set.items():
            if value > max_set_size:
                max_set_size = value
                max_set_key = key
            
        return self.uf.element_of_set[max_set_key]