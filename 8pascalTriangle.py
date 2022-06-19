"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/pascals-triangle/
Problem Statement:
Given an integer numRows, return the first numRows of Pascal's triangle.

Problem Solution:
"""


class Solution:
    @staticmethod
    def generate(numRows: int) -> list[list[int]]:
        pascal = [[1] * row for row in range(1, numRows+1)]

        for i in range(2, numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
        return pascal


sol = Solution()
print(sol.generate(5))
