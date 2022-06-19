"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/reshape-the-matrix/
Problem Statement:
Given a 2D Matrix, reshape it into a new one with a different size.

Problem Solution:

"""


class Solution:
    @staticmethod
    def matrix_reshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        # convert into a 1D array
        org_row_size = len(mat)
        org_col_size = len(mat[0])
        array_1d = []
        for i in range(0, org_row_size):
            for j in range(0, org_col_size):
                # print(f"{i},{j} | New Element at {(org_col_size * i + j)}")
                array_1d.append(mat[i][j])

        # check if conversion is legal
        if len(array_1d) < (r * c):
            return mat

        # convert 1D array into newly shaped 2D array.
        array_2d = [[0 for i in range(c)] for j in range(r)]
        for i in range(0, len(array_1d)):
            # calculate index to be placed in at i,j
            calc_i = int(i / c)
            calc_j = i % c
            print(f"{i} | New Element at {calc_i}, {calc_j}")
            array_2d[calc_i][calc_j] = array_1d[i]
        return array_2d


sol = Solution()
# input matrix
inMat = [[1, 1]]
out = sol.matrix_reshape(inMat, 1, 1)
print(out)
