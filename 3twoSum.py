"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/two-sum/
Problem Statement:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Problem Solution (in O(n)):
1: We can use a dict (hash table) to store previously visited values.
2: Calculate the value pair we need by using, need_val = target - current_val
3: look to see if we have this need_val in our dict
4: if we do, return need_val index and current_val index
   otherwise add the current_val to the dict and continue
"""


class Solution:
    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        # our dict
        seen_values = {}
        # loop through enumerated version of nums
        for i, value in enumerate(nums):
            need_val = target - value
            if need_val in seen_values:
                # return both index locations of need_val and value
                return [seen_values[need_val], i]
            # store in form of, key: element value in nums, value: index location in nums.
            seen_values[value] = i
        # return empty (no pairs found that meet target)
        return []


test = [2, 7, 11, 15]
tar = 9
sol = Solution()
print(f"{sol.two_sum(test, tar)}")
test = [3, 2, 4]
tar = 6
print(f"{sol.two_sum(test, tar)}")
test = [3, 3]
tar = 6
print(f"{sol.two_sum(test, tar)}")
