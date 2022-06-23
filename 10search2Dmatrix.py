"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/search-a-2d-matrix/
Problem Statement:
Given a sorted (left to right, top to bottom) 2D matrix, search for a target value.

Problem Solution:
1: Convert 2D matrix into 1D array.
2: Search for target
"""


class Solution:
    @staticmethod
    def search_matrix(matrix: list[list[int]], target: int) -> bool:
        # convert into 1D.
        tmp_list = list()
        for row in matrix:
            tmp_list += row
        # search array
        for x in tmp_list:
            if target == x:
                return True
        # target not found
        return False


sol = Solution()
inp = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
tar = 13
print(f"{sol.search_matrix(inp, tar)}")
