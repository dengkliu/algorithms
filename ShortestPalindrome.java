// Given a string S, you are allowed to convert it to a palindrome 
// by adding characters in front of it. 
// Find and return the shortest palindrome you can find by performing this transformation.

// Input: "aacecaaa"
// Output: "aaacecaaa"
// Explanation:
// add an 'a' in front of the input string.

// Need to find the longest palindrome starting at the first character
// We can enumerate the center
// The center must be at the first half
// We can use opposite two pointers to check palindrome.

public class Solution {
    /**
     * @param str: String
     * @return: String
     */
    // aacecaaa
    // aaceaa
    // abcd
    public String shortestPalindrome(String str) {

        int maxPalindromeLength = 0;

        for (int center = str.length()/2; center >= 0; center --) {
            maxPalindromeLength = Math.max(maxPalindromeLength,
                Math.max(extend(center, center, str), 
                         extend(center, center + 1, str)));
        }

        StringBuffer sb = new StringBuffer();

        for (int i = 0; i < str.length() - maxPalindromeLength; i ++) {
            sb.append(str.charAt(str.length() - i - 1));
        }

        return sb.toString() + str;
    }

    int extend(int left, int right, String str) {

        while (left >= 0 && right < str.length()) {
            if (str.charAt(left) == str.charAt(right)) {
                left --;
                right ++;
            } else {
                break;
            }
        }

        return left == - 1 ? right - left - 1 : -1; 
    }
}

