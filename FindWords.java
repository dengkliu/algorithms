// https://www.lintcode.com/problem/194/

// Given a string str and a dictionary dict, you need to find out which words in the dictionary are subsequences of the string and return those words.
// The order of the words returned should be the same as the order in the dictionary.

// |str|<=1000
// the sum of all words length in dictionary<=1000


// Input:
// str="bcogtadsjofisdhklasdj"
// dict=["book","code","tag"]
// Output:
// ["book"]
// Explanation:Only book is a subsequence of str

// 1. Brute force - two pointer
//    For each word, put a pointer at the head of the word, and another pointer at the head of the str
//    if the current character of the word is the same as the character in the str, then move both pointers to next character
//    otherwise just move the pointer for the str
//    Worst case: "abbaa" ["aaa", "aa", ....,] O(N*M) N - string length M - total number of words in the array
// 2. Use hash table to record the index for each character, so we avoid scanning the str
//    Each character may appear in multiple positions, so you need a list.
//    When scanning the word from the dictionary, you can do binary search to speed up further (find out whether there exists a number in the array
//    than target number)


public class Solution {
    /**
     * @param str: the string
     * @param dict: the dictionary
     * @return: return words which  are subsequences of the string
     */
    public List<String> findWords(String str, List<String> dict) {

        // HashMap<Character, Integer> is really a HashMap<Object, Object>. 
        // The compiler does a bunch of additional checks and implicit casts to make sure you don't put the wrong type of value in or get the wrong type out, 
        // but at runtime there is only one HashMap class and it stores objects.
        Map<Character, List<Integer>> charToIndex = new HashMap<>();

        char[] charArray = str.toCharArray();

        for (int i = 0; i < charArray.length; i ++) {
            Character character = Character.valueOf(charArray[i]);
            List<Integer> indexes = charToIndex.getOrDefault(character, new ArrayList<>());
            indexes.add(i); 
            charToIndex.put(character, indexes);
        }

        List<String> result = new ArrayList<>();

        for (String word : dict) {

            if(isValid(word, charToIndex)) {
                result.add(word);
            }
        }

        return result;
    }

    boolean isValid(String word, Map<Character, List<Integer>> charToIndex) {

        int previousCharPosition = -1;

        for (int i = 0; i < word.length(); i ++) {

            Character currentChar = Character.valueOf(word.charAt(i));

            if (!charToIndex.containsKey(currentChar)) {

                 System.out.println("Current char doesn't exist in map");

                return false;
            }

            List<Integer> positions = charToIndex.get(currentChar);

            System.out.println("Positions of current char " + currentChar + " in the string");

            for (Integer num : positions) {
                System.out.print(num + " ");
            }
            System.out.println(" ");
            
            previousCharPosition = findPosition(previousCharPosition, positions);

            if (previousCharPosition == -1) {
                return false;
            }

            System.out.println("Positions found for " + currentChar + " in the string is " + previousCharPosition);
        }

        return true;
    }

    // Find the minimum number greater than num
    int findPosition(int num, List<Integer> nums) {
                
        int start = 0;
        int end = nums.size() - 1;

        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            
            System.out.println(nums.get(start));
            System.out.println(nums.get(mid));
            System.out.println(nums.get(end));

            if (nums.get(mid) > num) {
                end = mid;
                continue;

            // because we are looking for a large time, 
            // we shouldn't break when we found an equal!!!!
            } else if (nums.get(mid) <= num) {
                start = mid;
                continue;
            }
        }

        System.out.println(nums.get(start));
        System.out.println(nums.get(end));

        if (nums.get(start) > num) {
            return nums.get(start);
        } 

        if (nums.get(end) > num) {
            return nums.get(end);
        }

        return -1;
    }
}