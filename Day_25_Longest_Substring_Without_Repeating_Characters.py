'''
Day 25 : Longest Substring Without Repeating Characters :

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
def lengthOfLongestSubstring(self, s):
    chara = {}
    start = 0
    mxlen = 0
    for i in range(len(s)):
        if s[i] in chara and chara[s[i]] >= start:
            start = chara[s[i]] + 1
        chara[s[i]] = i
        length = i - start  +1
        mxlen = max(mxlen , length)
    return mxlen