// https://www.lintcode.com/problem/1070


// Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

// Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

// After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

// The length of accounts will be in the range [1, 1000].
// The length of accounts[i] will be in the range [1, 10].
// he length of accounts[i][j] will be in the range [1, 30].

// Input:
// 	[
//		["John", "johnsmith@mail.com", "john00@mail.com"],
//		["John", "johnnybravo@mail.com"],
//		["John", "johnsmith@mail.com", "john_newyork@mail.com"],
//		["Mary", "mary@mail.com"]
//	]
//	
//	Output: 
//	[
//		["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
//		["John", "johnnybravo@mail.com"],
//		["Mary", "mary@mail.com"]
//	]

//	Explanation: 
//	The first and third John's are the same person as they have the common email "johnsmith@mail.com".
//	The second John and Mary are different people as none of their email addresses are used by other accounts.

//	You could return these lists in any order, for example the answer
	
//	[
//		['Mary', 'mary@mail.com'],
//		['John', 'johnnybravo@mail.com'],
//		['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
//	]
//	is also acceptable.


class UnionFind {

    // Mapping from root to the emails in the set
    private Map<String, List<String>> emailsInSet;

    // Mapping from email to root
    private Map<String, String> parents;

    UnionFind() {
        emailsInSet = new HashMap<>();
        parents = new HashMap<>();
    }

    public Map<String, List<String>> getEmailsInSet() {
        return emailsInSet;
    }

    public void add(String email) {
        if (parents.containsKey(email)) {
            return;
        }

        parents.put(email, null);
        // Each set contians the emails by itself

        List<String> emails = new ArrayList<>();
        emails.add(email);

        emailsInSet.put(email, emails);
    }

    public String find(String email) {

        // If the emails maps to null, the root is itself.
        String root = email;

        while (parents.get(root) != null) {
            root = parents.get(root);
        }

        // Path compression, to make it real O(1)
        while(!email.equals(root)) {
            String previousParent = parents.get(email);
            parents.put(email, root);
            email = previousParent;
        }

        return root;
    }

    public void union(String email1, String email2) {
        
        String root1 = find(email1);
        String root2 = find(email2);

        // String comparision using equals!
        if (root1.equals(root2)) {
            return;
        }

        parents.put(root1, root2);

        List<String> root2Emails = emailsInSet.get(root2);
        root2Emails.addAll(emailsInSet.get(root1));

        emailsInSet.put(root2, root2Emails);
        emailsInSet.remove(root1);
    }
}


public class Solution {
    /**
     * @param accounts: List[List[str]]
     * @return: return a List[List[str]]
     */
    public List<List<String>> accountsMerge(List<List<String>> accounts) {

        Map<String, String> emailToName = new HashMap<>();
        
        // write your code here
        List<List<String>> sortedEmailsByAccount = new ArrayList<>();

        UnionFind uf = new UnionFind();

        if (accounts == null || accounts.size() == 0) {
            return sortedEmailsByAccount;
        }

        for (int i = 0; i < accounts.size(); i ++) {

            List<String> currentAccounts = accounts.get(i);

            for (int j = 1; j < currentAccounts.size(); j ++) {
                String currentAccount = currentAccounts.get(j);

                emailToName.put(currentAccount, currentAccounts.get(0));

                uf.add(currentAccount);

                if (j == 1) {
                    continue;
                }

                // Always union the email with the first email address
                // Set the first email address as root
                uf.union(currentAccount, currentAccounts.get(1));
            }
        }

        for (String email : uf.getEmailsInSet().keySet()) {
            List<String> currentEmails = new ArrayList<>();

            // First add the name for the email
            currentEmails.add(emailToName.get(email));

            // Get the emails that are in the same set as this email
            List<String> currentEmailSet = uf.getEmailsInSet().get(email);

            // Sort
            Collections.sort(currentEmailSet);

            currentEmails.addAll(currentEmailSet);

            sortedEmailsByAccount.add(currentEmails);
        } 

        return sortedEmailsByAccount;

    }
}

