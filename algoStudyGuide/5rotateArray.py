"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/rotate-array/

Problem Statement:
Given an array, rotate the array to the right by k steps, where k is non-negative.

Problem Solution:
Can use python's ability to shape lists and a bit of math to solve.
Think of grabbing a left and a right side and reversing the two.
To get the items on the right side (to put in first) we can calculate the first index to be
n - (k mod n) where n = length of list and k number of times to shift.
To get items on the left side (to put in after the right side) we use the previous value.
"""


class Solution:
    @staticmethod
    def rotate(nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        print(f"{n - k % n} where n={n}, k={k} and k%n={k%n}")
        print(f"{nums[n - k % n:]}")
        print(f"{nums[0:n - k % n]}")
        nums[:] = nums[n - k % n:] + nums[0:n - k % n]


sol = Solution
nums_in = [1, 2, 3, 4, 5, 6, 7]
steps = 3
sol.rotate(nums_in, steps)
print(f"{nums_in}")
