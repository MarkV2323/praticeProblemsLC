"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/maximum-subarray/
Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Problem Solution:
Use a "Sliding Window" Pattern for the problem for O(n^2) runtime,
https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed
Use Kadane's Algorithm for O(n) runtime,
https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

"""


class Solution:
    @staticmethod
    # Using Kadane's Algorithm (Dynamic Programming)
    def max_sub_array2(nums: list[int]) -> int:
        cur = nums[0]
        ret = cur
        for num in nums[1:]:
            cur = max(num, cur+num)
            ret = max(ret, cur)
        return ret

    @staticmethod
    # Brute Force version
    def max_sub_array(nums: list[int]) -> int:
        max_value = -10
        cur_win_size = 1
        current_value = 0
        for x in range(0, len(nums)):

            # creation of sub-array's with this window size.
            for y in range(0, len(nums) - x):

                # y - represents the starting index for this sub array.
                # cur_win_size - how many elements to add to the sub array.
                # z - how many elements to add into the sub array.
                for z in range(0, cur_win_size):
                    current_value += nums[y + z]

                # check if this is the largest sub array sum found.
                if current_value > max_value:
                    max_value = current_value

                # reset the current_value
                current_value = 0

            # increase cur_win_size by 1.
            cur_win_size += 1

        return max_value


# create solution object
solution = Solution()
# Test Cases
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1]
nums3 = [5, 4, -1, 7, 8]
# # run cases
# case1 = solution.max_sub_array(nums1)
# case2 = solution.max_sub_array(nums2)
# case3 = solution.max_sub_array(nums3)
# # print results
# print(f"Case 1: {nums1} has max sub array value: {case1}")
# print(f"Case 2: {nums2} has max sub array value: {case2}")
# print(f"Case 3: {nums3} has max sub array value: {case3}")
case1 = solution.max_sub_array2(nums1)
case2 = solution.max_sub_array2(nums2)
case3 = solution.max_sub_array2(nums3)
print(f"Case 1: {nums1} has max sub array value: {case1}")
print(f"Case 2: {nums2} has max sub array value: {case2}")
print(f"Case 3: {nums3} has max sub array value: {case3}")
