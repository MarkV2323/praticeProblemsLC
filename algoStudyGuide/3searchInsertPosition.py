"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/search-insert-position/

Problem Statement:
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Problem Solution:
This is simply a binary search with a different return value for a missing value.
Rather than return -1, we can just return the left bound index as that is where the target should be inserted.
"""


class Solution:
    @staticmethod
    # implement binary search
    def search(nums: list[int], target: int) -> int:
        left_bound = 0
        right_bound = len(nums) - 1
        # stop if left_bound exceeds right_bound
        while left_bound <= right_bound:
            # calculate middle index
            mid_index = (left_bound + right_bound) // 2
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] < target:
                # target is larger, ignore left half
                left_bound = mid_index + 1
            else:
                # target is smaller, ignore right half
                right_bound = mid_index - 1
        # return indie where target should be inserted.
        return left_bound


sol = Solution()
tar = 7
arr1 = [1, 3, 5, 6]
print(f"found target at index: {sol.search(arr1, tar)}")