
class TrieNode {

	// 这个node连到children的边上是什么character
	// 一个node可以有多个children
	public Map<Character, TrieNode> children;

	public boolean isWord;

	public String word;

	public TrieNode() {
		children = new HashMap<Character, TrieNode>();
		isWord = false;
		word = null;
	}
}

class Trie {

	private TrieNode root;

	public Trie() {
		root = new TrieNode();
	}

	public TrieNode getRoot() {
		return root;
	}

	public void insert(String word) {

		TrieNode node = root;

		for (int i = 0; i < word.length(); i++) {

			char letter = word.charAt(i);

			// 需要查重，如果这个character已经在trie中了
			// 直接往下移就行
			if (!node.children.containsKey(letter)){
				TrieNode newNode = new TrieNode();
				node.children.put(word.charAt(i), newNode);
			}

			node = node.children.get(letter);
		}

		node.isWord = true;
		node.word = word;
	}
}

public class WordDictionary {

    Trie trie = new Trie();

    /*
     * @param word: Adds a word into the data structure.
     * @return: nothing
     */
    public void addWord(String word) {
        trie.insert(word);
    }

    /*
     * @param word: A word could contain the dot character '.' to represent any one letter.
     * @return: if the word is in the data structure.
     */
    public boolean search(String word) {

        return dfs(trie.getRoot(), word, 0);
    }

    boolean dfs(TrieNode root, String word, int index) {

        if (index == word.length()) {
            return root.isWord;
        }

        Character currentChar = word.charAt(index);

        if (currentChar == '.') {
            for (Character c : root.children.keySet()) {

                // 只要有一个路径能走通，就return true
                if (dfs(root.children.get(c), word, index + 1)) {
                    return true;
                };
            }

            return false;
        }

        if (root.children.containsKey(currentChar)) {
            return dfs(root.children.get(currentChar), word, index + 1);
        }

        return false;
    }
}