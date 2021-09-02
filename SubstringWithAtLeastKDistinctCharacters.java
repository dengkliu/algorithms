// https://www.lintcode.com/problem/1375
// Given a string S with only lowercase characters.
// Return the number of substrings that contains at least k distinct characters.

// 10 ≤ length(S) ≤ 1,000,00010≤length(S)≤1,000,000
// 1 ≤ k ≤ 261≤k≤26

// 1. Brute-force - enumerate all substrings, and count of the number of unique characters. Worst case O(N^3)
// 2. 

public class Solution {
    /**
     * @param s: a string
     * @param k: an integer
     * @return: the number of substrings there are that contain at least k distinct characters
     */
    public long kDistinctCharacters(String s, int k) {
        int end = 0;
        long result = 0l;
        int numOfUniqueChar = 0;

        Map<Character, Integer> charCountMap = new HashMap<>();

        for (int start = 0; start < s.length(); start ++) {

            while (end < s.length() && numOfUniqueChar < k) {

                Character currentChar = Character.valueOf(s.charAt(end));

                int occurrence = charCountMap.getOrDefault(currentChar, 0);

                if (occurrence == 0) {
                    numOfUniqueChar ++;
                }

                charCountMap.put(currentChar, occurrence + 1);
                end ++;
            }

            if (end == s.length() && numOfUniqueChar < k) {
                break;
            }

            if (numOfUniqueChar == k) {
                result = result + s.length() - end + 1;
            }

            int countOfStartChar = charCountMap.get(s.charAt(start));

            if (countOfStartChar == 1) {
                numOfUniqueChar--;
            }

            charCountMap.put(s.charAt(start), countOfStartChar - 1);
        }

        return result;
    }
}
