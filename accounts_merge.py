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
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # cache all unique emails. why do we need this set
        # beyond the graph above?
        emails = set()
        email_to_name = {}

        # all emails connected to each other
        graph = collections.defaultdict(list)
        for account in accounts:
            for x in range(1, len(account)):
                email1 = account[x]
                emails.add(email1)
                email_to_name[email1] = account[0]
                for y in range(x + 1, len(account)):
                    email2 = account[y]
                    graph[email1].append(email2)
                    graph[email2].append(email1)

        visited = set()

        def bfs(email):
            queue = collections.deque()
            queue.append(email)
            visited.add(email)
            connected_emails = []
            connected_emails.append(email)

            while queue:
                cur = queue.popleft()
                for next_e in graph[cur]:
                    if next_e not in visited:
                        queue.append(next_e)
                        visited.add(next_e)
                        connected_emails.append(next_e)

            return connected_emails

        result = []

        for email in emails:
            if email not in visited:
                visited.add(email)
                connected_emails = bfs(email)
                connected_emails.sort()
                result.append([email_to_name[email]] + connected_emails)
        
        return result
                
