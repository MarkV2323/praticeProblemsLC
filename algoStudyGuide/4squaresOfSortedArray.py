"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/squares-of-a-sorted-array/

Problem Statement:
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Problem Solution:

"""


class Solution:
    @staticmethod
    def sorted_squares(nums: list[int]) -> list[int]:
        left_p, right_p, r_list = 0, len(nums) - 1, list()

        while left_p <= right_p:
            # check pointers
            if abs(nums[left_p]) <= abs(nums[right_p]):
                r_list.append((nums[right_p] ** 2))
                right_p -= 1
            else:
                r_list.append((nums[left_p] ** 2))
                left_p += 1

        return r_list[::-1]


nums_inp = [-4, -1, 0, 3, 10]
sol = Solution
print(f"{sol.sorted_squares(nums_inp)}")
