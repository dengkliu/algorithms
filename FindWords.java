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
// 2. Use hash table to record the index for each character
//    