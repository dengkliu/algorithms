class TrieNode {

    private Map<Character, TrieNode> children;

    private boolean hasWord;

    private String word;

    Map<Character, TrieNode> getChidren() {
        return this.children;
    }

    boolean hasWord() {
        return hasWord;
    }

    void setHasWord(boolean hasWord) {
        this.hasWord = hasWord;
    }

    String getWord() {
        return word;
    }

    void setWord(String word) {
        this.word = word;
    }

    TrieNode() {
        children = new HashMap<>();
        hasWord = false;
        word = null;
    }
}


public class Trie {

    private TrieNode root;

    public TrieNode getRoot() {
        return root;
    }

    public Trie() {
        root = new TrieNode();
    }

    /*
     * @param word: a word
     * @return: nothing
     */
    public void insert(String word) {

        TrieNode node = root;

        for (int i = 0; i < word.length(); i++) {
            Character currChar = word.charAt(i);
            Map<Character, TrieNode> children = node.getChidren();

            if (!children.containsKey(currChar)) {
                TrieNode nextNode = new TrieNode();
                children.put(currChar, nextNode);
            }

            node = children.get(currChar);
        }

        node.setHasWord(true);
        node.setWord(word);
    }

    /*
     * @param word: A string
     * @return: if the word is in the trie.
     */
    public boolean search(String word) {

        TrieNode node = root;

        for (int i = 0; i < word.length(); i++) {

            Character currChar = word.charAt(i);
            Map<Character, TrieNode> children = node.getChidren();

            if (!children.containsKey(currChar)) {
                return false;
            }

            node = children.get(currChar);
        }

        return node.hasWord();
    }

    /*
     * @param prefix: A string
     * @return: if there is any word in the trie that starts with the given prefix.
     */
    public boolean startsWith(String prefix) {
         TrieNode node = root;

        for (int i = 0; i < prefix.length(); i++) {

            Character currChar = prefix.charAt(i);
            Map<Character, TrieNode> children = node.getChidren();

            if (!children.containsKey(currChar)) {
                return false;
            }

            node = children.get(currChar);
        }

        return true;
    }

    /*
     * @param word: A string
     * @return: the trie node where the word ends
     */
    public TrieNode searchWordNodePos(String word) {

        TrieNode node = root;

        for (int i = 0; i < word.length(); i++) {

            Character currChar = word.charAt(i);
            Map<Character, TrieNode> children = node.getChidren();

            if (!children.containsKey(currChar)) {
                return null;
            }

            node = children.get(currChar);
        }

        if (node.hasWord()) {
            return node;
        };
        
        return null;
    }
}