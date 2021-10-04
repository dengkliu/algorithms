# https://www.lintcode.com/problem/1396

# There is a list composed by sets. If two sets have the same elements, merge them. Returns the last remaining collection.
# The number of sets n <=1000.
# The number of elements for each set m <= 100.
# The element must be a non negative integer and not greater than 100000.

# Input:list = [[1],[1,2,3],[4],[8,7,4,5]]
# Output :2
# Explanation:There are 2 sets of [1,2,3] and [4,5,7,8] left.

# Use union find, it automatically deals with solving duplicate and union
# Use the first element of each sets as root
# Time complexity - O(N*M) N - number of sets M - avg number of integers in all sets


class UnionFind:
    
    def __init__(self):
        self.father = {}
        self.num_of_sets = 0
    
    def add(self, x):  
        if x in self.father:
            return
            
        self.father[x] = None
        self.num_of_sets += 1
    
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
        self.num_of_sets -= 1
    

class Solution:

    def __init__(self):
        self.uf = UnionFind()

    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        
        if not sets or len(sets) == 0:
            return 0

        for i in range(len(sets)):
            curr_set = sets[i]
            for j in range(len(curr_set)):
                self.uf.add(curr_set[j])
                self.uf.merge(curr_set[j], curr_set[0])

        return self.uf.num_of_sets

