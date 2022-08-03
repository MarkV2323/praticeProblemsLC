"""
Problem can be found at: https://leetcode.com/problems/valid-palindrome/submissions/
"""


class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        # convert to lowercase, replace whitespace.
        tmp = s.lower()
        tmp = tmp.replace(" ", "")

        # check edge case
        if len(tmp) == 0:
            return True

        # remove all non alpha characters
        tmp = ''.join(filter(str.isalnum, tmp))

        # create reversed version of tmp
        r_tmp = ""
        for x in tmp[::-1]:
            r_tmp += x

        # print(tmp)
        # print(r_tmp)
        if tmp == r_tmp:
            return True

        return False


sol = Solution()
print(sol.is_palindrome("0P"))
