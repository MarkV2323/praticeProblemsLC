"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/squares-of-a-sorted-array/

Problem Statement:
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Problem Solution:
Use two pointers, one from the start and one from the end, call these left and right pointers

Compare nums elements at pointer values, nums has the following criteria
1 - sorted in descending order (from least to greatest)
2 - can contain negative numbers

As a result, compare the absolute values of the input list's elements.

if the left pointer value is less than or equal to the right pointer value,
append the right value squared to the return list and move the right pointer by 1 element

else append the left value squared to the return list and move the left pointer by 1 element

By always appending the larger value, we are guaranteeing that our return list is in decreasing order.
Before returning, we can just flip the order (now non-decreasing) to meet the requirement.
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
