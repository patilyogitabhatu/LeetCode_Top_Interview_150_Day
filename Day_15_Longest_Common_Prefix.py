'''
Day 15 : Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
def longestCommonPrefix(self, strs):
        ans=""
        strs=sorted(strs)
        left=strs[0]
        right=strs[-1]
        for i in range(min(len(left),len(right))):
            if left[i]!=right[i]:
                return ans
            ans +=left[i]
        return ans 