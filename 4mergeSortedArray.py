"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/merge-sorted-array/
Problem Statement:
Given two integers arrays, sorted in non-decreasing order, and two integers,
merge the two arrays into a single array sorted in non-decreasing order.

Problem Solution:
1: Append second array onto the end of the first array.
2: Use sort algorithm to sort into non-decreasing order. 
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # append nums2 onto end of nums1
        n_p = 0
        for i in range(m, m+n):
            nums1[i] = nums2[n_p]
            n_p += 1
        # apply timsort to nums1.
        nums1.sort()


sol = Solution()
# Test Case
num1 = [4, 5, 6, 0, 0, 0]
m1 = 3
num2 = [1, 2, 3]
n1 = 3
# Expected output: [1, 2]
sol.merge(num1, m1, num2, n1)
print(f"OUTPUT: {num1}")
