// 字典树压缩公共前缀

clas TrieNode {

	// 这个node连到children的边上是什么character
	// 一个node可以有多个children
	private Map<Character, TrieNode> children;

	private boolean isWord;

	private String word;

	public Map<Character, TrieNode> getChildren() {
		return this.children;
	}

	public boolean isWord() {
		return this.isWord;
	}

	public String word() {
		return this.word;
	}

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