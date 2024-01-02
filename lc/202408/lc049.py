"""
LC 49: Group Anagram

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""
# 15
def group_anagrams(strs):
    groups = {}
    for s in strs:
        groups.setdefault(tuple(sorted(s)), []).append(s)
    return [v for _, v in groups.items()]

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


strs = [""]
print(group_anagrams(strs))
# Output: [[""]]

strs = ["a"]
print(group_anagrams(strs))
# Output: [["a"]]
