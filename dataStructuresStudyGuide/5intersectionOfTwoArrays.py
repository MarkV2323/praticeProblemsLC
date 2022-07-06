"""
Author: Mark Vincent II
For LeetCode problem:
Problem Statement:
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays,
and you may return the result in any order.

Problem Solution:
1: Convert each list into a dict with key being the value, and the value being the total count.
2: Check if key is in other dict, if so, append the key to return list the minimum count from both dicts.
"""


class Solution:
    @staticmethod
    def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
        # python has built "Counter" collection that does the same thing.
        # convert nums1 into dict
        dic_n1 = {}
        for value in nums1:
            if value not in dic_n1:
                dic_n1[value] = 1
            else:
                dic_n1[value] += 1
        # convert nums2 into dict
        dic_n2 = {}
        for value in nums2:
            if value not in dic_n2:
                dic_n2[value] = 1
            else:
                dic_n2[value] += 1
        # build list
        r_list = list()
        for key in dic_n1.keys():
            if key in dic_n2:
                # append key depending on lowest amount of times seen.
                for i in range(0, min(dic_n1.get(key), dic_n2.get(key))):
                    r_list.append(key)
        # return list
        return r_list


sol = Solution()
l1 = [4, 9, 5]
l2 = [9, 4, 9, 8, 4]
print(f"RETURN LIST: {sol.intersect(l1, l2)}")
