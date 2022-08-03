"""
Can be found at:
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Need to go over again sometime.
"""


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        dic = {}
        max_len = 0
        start = -1

        # loop through each char in string.
        for i, c in enumerate(s):

            # if char has been seen before,
            # - set prev value to dic value using char as key
            # - set start to max value between prev and start.
            print(f"{i}, {c}")
            if c in dic:
                prev = dic[c]
                start = max(prev, start)

            # dic key is the char, dict value is index
            dic[c] = i

            # get max len from max between current max_len and index minus the start index.
            max_len = max(max_len, i - start)

        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstring("aab"))
