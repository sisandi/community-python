"""
Given two sequences, x[1:m] and y[1:n],
find a longest sequence common to both. Uses memoization
to store intermediate results so comparisons between same
string indices are not duplicated

BASE CASE:
There are no letters in one string to compare

CASE 1:
The last letter of P and Q are the same

CASE 2:
The last letter of P and Q are different
"""

from datetime import datetime


class Solution:

    def __init__(self):
        self.matrix = {}

    def longestCommonSubsequence(self, P: str, Q: str) -> int:

        n = len(P)
        m = len(Q)

        result = 0
        keyy = f'{n - 1},{m - 1}'
        if keyy in self.matrix.keys():
            return self.matrix[keyy]

        # BASE CASE
        if n == 0 or m == 0:
            result = 0

        # CASE 1
        elif P[n - 1] == Q[m - 1]:
            result = 1 + self.longestCommonSubsequence(P[:-1], Q[:-1])

        # CASE 2
        elif P[n - 1] != Q[m - 1]:
            tmp1 = self.longestCommonSubsequence(P[:-1], Q)
            tmp2 = self.longestCommonSubsequence(P, Q[:-1])
            result = max(tmp1, tmp2)

        self.matrix[f'{n - 1},{m - 1}'] = result
        return result


x = "alibnalwieefasdfv"
y = "wliheglaijwegasv"


start = datetime.now()
t = Solution()
print(t.longestCommonSubsequence(x, y))

end = datetime.now()
delta = end-start
print(delta)
