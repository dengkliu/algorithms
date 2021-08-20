// https://www.lintcode.com/problem/333
// Given n character strings containing only lower case letters, find the minimum prefix strings that can identify each string.
// That is, the minimum prefix string Ap which identifies string A will not be a prefix string of other n-1 character strings.

// 1 <= n <= 500
// The length of strings would not exceed 100.
// If string S is a profix of string T, the answer of S will be itself.

// Input:["aaa","bbc","bcd"]
// Output:["a","bb","bc"]
// Explanation:"a" is only the profix of "aaa".
// "bb" is only the profix of "bbc".
// "bc" is only the profix of "bcd".

// String + prefix ---> definitely use trie!
// How to determine the identifying prefix?


// ["adf", "ace", "acd"]
// root -- a -- > node1 --- b ---> node2 --f-> node3 (word)
//                  |                    
//                  c 
//                  |
//                 node4 --- d ---> node5 (word)
//                  |
//                  e
//                  |
//                 node6 (word) 
// 
// ["aa", "aaa"]
// 
// root -- a --> node1 -- a --> node2 (word) -- a --> node3 -- a --> node4 (word)
//    
// 1. for a given word and its path on the trie, you always needs to find the last node
//    that has one more chidren, until the end. Include the edge from that node in the prefix.
// 2. for a given word, if its a prefix for other word, then its identifying string is itself.
//    for the word that contains this word as prefix, the minimum identifying prefix would include one more letter
//                   
class TrieNode {

    private Map<Character, TrieNode> children;
    private boolean isWord;
    private String word;

    Map<Character, TrieNode> getChildren() {
        return children;
    }

    boolean isWord() {
        return isWord;
    }

    void setIsWord(boolean isWord) {
        this.isWord = isWord;
    } 

    void setWord(String word) {
        this.word = word;
    }

    String getWord() {
        return word;
    }

    TrieNode() {
        children = new HashMap<>();
        isWord = false;
        word = null;
    }
}


class Trie {

    private TrieNode root;

    Trie() {
        root = new TrieNode();
    }

    TrieNode getRootNode() {
        return root;
    }

    void insertWord(String word) {

        TrieNode current = root;

        for(int i = 0; i < word.length(); i++) {

            char currentChar = word.charAt(i);

            if (current.getChildren().containsKey(currentChar)) {
                current = current.getChildren().get(currentChar);
                continue;
            }

            current.getChildren().put(currentChar, new TrieNode());
            current = current.getChildren().get(currentChar);
        }

        current.setIsWord(true);
        current.setWord(word); 
    }
}


public class Solution {
    /**
     * @param stringArray: a string array
     * @return: return every strings'short peifix
     */
    public String[] ShortPerfix(String[] stringArray) {

        if (stringArray == null) {
            return null;
        }

        int n = stringArray.length;

        Trie trie = new Trie();

        for (int i = 0; i < n; i ++) {
            trie.insertWord(stringArray[i]);
        }

        String[] result = new String[stringArray.length];

        for (int i = 0; i < n; i++) {
            String currentString = stringArray[i];
            result[i] = findIdentifyPrefix(currentString, trie);
        }

        return result;
    }

    String findIdentifyPrefix(String str, Trie trie) {
       
       TrieNode currentNode = trie.getRootNode();

       int end = 0;

       // root - "a" -> node1 - "a" -> node2 (word) - "a" -> node3...
       for (int i = 0; i < str.length(); i++) {

           Character currChar = str.charAt(i);
           TrieNode nextNode = currentNode.getChildren().get(currChar);
           
            // 找到最后的那个分叉
           if(nextNode.getChildren().size() > 1) {
               end = i + 1;
           }

           if (nextNode.isWord()) {
               // 如果找到了当前str
               if (nextNode.getWord().equals(str)) {
                   // 如果当前str是其他str的前缀 那么它的最小前缀是自己本身
                   if (nextNode.getChildren().size() > 0) {
                       end = str.length() - 1;
                    }
                    // 已经找到玩当前str 直接退出
                    break;
                }

                // 如果不是当前str,那么要重设end, end至少要比现在找到的这个str多一个char
                end = nextNode.getWord().length();
           }

           currentNode = nextNode;
       }

       return str.substring(0, end + 1);

    }
}