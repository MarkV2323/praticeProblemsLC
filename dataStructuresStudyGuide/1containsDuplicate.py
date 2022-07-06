"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/contains-duplicate/
Problem Statement: If any value in the list appears at least twice, return false, else return true.
Problem Solution:
1: Use a built-in python set to keep track of seen elements.
2: Iterate from start of list, check if current element belongs to the set.
3: If it does, a duplicate has been found, else, add the element to the set and move on to the next iteration.
4: Once we have traversed the entire list, return False because no duplicates are found.
"""


class Solution:
    @staticmethod
    def contains_duplicate(nums: list[int]) -> bool:
        # Create a set object. (Python sets underlying DS is a Hash Table)
        tmp_set = set()
        # begin looping through the array (list).
        for element in nums:
            # check if element belongs to tmp_set
            if element in tmp_set:
                # duplicate has been found!
                return True
            else:
                # store element in set to keep track of what has been added so far.
                tmp_set.add(element)
        # no duplicates found.
        return False


# Test Cases
# true
nums1 = [1, 2, 3, 1]
# false
nums2 = [1, 2, 3, 4]
# true
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
solution = Solution()
# run cases
case1 = solution.contains_duplicate(nums1)
case2 = solution.contains_duplicate(nums2)
case3 = solution.contains_duplicate(nums3)
# print results
print(f"Case 1: {nums1} contains duplicates: {case1}")
print(f"Case 1: {nums2} contains duplicates: {case2}")
print(f"Case 1: {nums3} contains duplicates: {case3}")
