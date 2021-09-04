// https://www.lintcode.com/problem/384/
// Given a string, find the length of the longest substring without repeating characters.
// Input: "abcabcbb"
// Output: 3
// Explanation: The longest substring is "abc"

// 典型的不确定range长度的substring问题 用同向双指针解决

public class Solution {
    /**
     * @param s: a string
     * @return: an integer
     */
    public int lengthOfLongestSubstring(String s) {

        if (s == null || s.length() == 0) {
            return 0;
        }

        int end = 0;
        
        Set<Character> charSet = new HashSet<>();

        int result = 1;

        for (int start = 0; start < s.length(); start ++) {

            while(end < s.length() && !charSet.contains(s.charAt(end))) {
                charSet.add(s.charAt(end));
                end ++;
            }

            if (end == s.length()) {
                result = Math.max(result, end - start);
                break;
            }

            result = Math.max(result, end - start);
            charSet.remove(s.charAt(start));      
        }

        return result;
    }
}