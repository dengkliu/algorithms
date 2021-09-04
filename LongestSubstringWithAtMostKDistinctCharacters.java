// https://www.lintcode.com/problem/386

// Given a string S, find the length of the longest substring T that contains at most k distinct characters.

// Input: S = "eceba" and k = 3
// Output: 4
// Explanation: T = "eceb"

// 典型不确定range的满足一定条件的substring问题 用同向双指针

public class Solution {
    /**
     * @param s: A string
     * @param k: An integer
     * @return: An integer
     */
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        
        if (s == null || s.length() == 0) {
            return 0;
        }

        // Edge case
        if (k == 0) {
            return 0;
        }

        int end = 0;
        
        Map<Character, Integer> charToCountMap = new HashMap<>();

        int result = 0;

        for (int start = 0; start < s.length(); start ++) {

            while(end < s.length() && charToCountMap.size() <= k) {
                int num = charToCountMap.getOrDefault(s.charAt(end), 0);
                num ++;
                charToCountMap.put(s.charAt(end), num);
                end ++;
            }

            if (end == s.length() && charToCountMap.size() <= k) {
                result = Math.max(result, end - start);
                break;
            }
            
            if (charToCountMap.size() > k) {
                result = Math.max(result, end - start - 1);
            }

            int num = charToCountMap.get(s.charAt(start));
            
            if (num == 1) {
                charToCountMap.remove(s.charAt(start));    
            } else {
                charToCountMap.put(s.charAt(start), num - 1);
            }
        }

        return result;
    }
}