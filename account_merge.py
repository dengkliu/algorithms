# https://www.lintcode.com/problem/1070

# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# he length of accounts[i][j] will be in the range [1, 30].

# Input:
# 	[
#		["John", "johnsmith@mail.com", "john00@mail.com"],
#		["John", "johnnybravo@mail.com"],
#		["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#		["Mary", "mary@mail.com"]
#	]
#	
#	Output: 
#	[
#		["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
#		["John", "johnnybravo@mail.com"],
#		["Mary", "mary@mail.com"]
#	]

#	Explanation: 
#	The first and third John's are the same person as they have the common email "johnsmith@mail.com".
#	The second John and Mary are different people as none of their email addresses are used by other accounts.

#	You could return these lists in any order, for example the answer
	
#	[
#		['Mary', 'mary@mail.com'],
#		['John', 'johnnybravo@mail.com'],
#		['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
#	]
#	is also acceptable.
class UnionFind:

    def __init__(self):
        self.father = {}
        self.elements_in_set = {}
    
    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.elements_in_set[x] = [x]

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.elements_in_set[root_y] += self.elements_in_set[root_x]
            del self.elements_in_set[root_x]
            
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        return root

class Solution:

    def __init__(self):
        self.uf = UnionFind()
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):

        if not accounts or len(accounts) == 0:
            return []
    
        account_to_name = {}
        # write your code here

        for i in range(len(accounts)):
            row = accounts[i]
            for j in range(1, len(row)):
                account_to_name[row[j]] = row[0]
                self.uf.add(row[j])
                self.uf.merge(row[j], row[1])
            
        result = []
        
        for key, value in self.uf.elements_in_set.items():
            value.sort()
            curr_person = []
            curr_person.append(account_to_name[key])
            curr_person += value
            result.append(curr_person)

        return result
