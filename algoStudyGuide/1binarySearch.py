"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/binary-search/

Problem Statement:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Problem Solution:
1: Problem statement calls for binary search to be implemented because,
Binary Search is O(log n) run time.
Binary Search requires a sorted array.
Implementation details:
2a - Start in middle of array as search key.
2b - Check value of search key vs target,
     if equal return index,
     elif less than the new search key will be the middle of the lower half interval
     elif greater than the new search key will be the middle of the upper half interval
     if interval is empty, return -1

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
        # target not found
        return -1


sol = Solution()
tar = 7
arr1 = [1, 2, 3, 4, 5, 6, 7]
print(f"found target at index: {sol.search(arr1, tar)}")

