clas TrieNode {

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

		for (int i = 0; i < word.length; i++) {

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
		node.isWord = word;
	}
}