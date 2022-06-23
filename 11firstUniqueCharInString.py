"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/first-unique-character-in-a-string/
Problem Statement:
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Problem Solution:
1: loop through given string.
2: Check current character vs string slices to see if it doesn't repeat, return if it doesn't.
"""


class Solution:
    @staticmethod
    def first_uniq_char(s: str) -> int:
        for i, c in enumerate(s):
            if (c not in s[i+1:]) and (c not in s[:i]):
                return i
        return -1


sol = Solution()
t = "leetcode"
print(f"{t}: {sol.first_uniq_char(t)}")
