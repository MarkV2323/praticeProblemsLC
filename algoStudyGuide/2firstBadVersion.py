"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/first-bad-version/

Problem Statement:
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version.
You should minimize the number of calls to the API.

Problem Solution:
Basically a game of, "guess the number I am thinking of, higher or lower".
Want to make it efficient though, can be modeled off of binary search, look at the mid-points.
"""


class Solution:
    @staticmethod
    def isBadVersion(version):
        bad_ver = 4
        if version >= bad_ver:
            return True
        return False

    @staticmethod
    def firstBadVersion(n: int) -> int:
        left_bound = 0
        right_bound = n
        idx = n // 2
        while left_bound <= right_bound:
            mid_version = (left_bound + right_bound) // 2
            if Solution.isBadVersion(mid_version):
                # Bad version found
                right_bound = mid_version - 1
                idx = mid_version
            else:
                # Good version found
                left_bound = mid_version + 1
        return idx


sol = Solution
print(f"First Bad Version at: {sol.firstBadVersion(5)}")
