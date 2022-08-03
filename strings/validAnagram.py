"""
Can be found at:
https://leetcode.com/problems/valid-anagram/submissions/
"""


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        # Easy method to finding anagrams is to sort both strings and compare values.
        tmpA = [s[i] for i in range(0, len(s))]
        tmpB = [t[i] for i in range(0, len(t))]

        # check if len is the same
        if len(tmpA) != len(tmpB):
            return False

        # try out sort (timsort is pythons default, is O(nlogn))
        tmpA.sort()
        tmpB.sort()

        # compare
        for i in range(0, len(tmpA)):
            print(f"{tmpA[i]} vs {tmpB[i]} at index {i}")
            if tmpA[i] != tmpB[i]:
                return False

        # must be an anagram
        return True


sol = Solution()
print(sol.isAnagram("rat", "car"))
