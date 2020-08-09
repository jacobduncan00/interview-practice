# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        outerArr = []
        for word in strs:
            wordLength = len(word) + 1
            for num in range(wordLength):
                wordFrag = word[:num]
                wordFragArr = []
                for word in strs:
                    if wordFrag in word:
                        wordFragArr.append(wordFrag)

                if len(wordFragArr) == len(strs):
                    outerArr = wordFragArr



        if outerArr == []:
            return ""
        else: 
            return outerArr[0]




test = Solution()
print("1", test.longestCommonPrefix(["gopher", "golang", "gone"]))
print("2", test.longestCommonPrefix(["a"]))
print("3", test.longestCommonPrefix(["aaa", "aa", "aaa"]))
print("4", test.longestCommonPrefix(["ca", "a"]))

# This is the most bullshit problem, either I'm brain dead or this is some weird
# Python Regex shit. Anyways, worked on it off and on for about 2 hours and
# still couldn't get it to pass on LEETCODE
