# """
# Given two sequences, x[1:m] and y[1:n],
# find a longest sequence common to both. Uses memoization
# to store intermediate results so comparisons between same
# string indices are not duplicated
#
# BASE CASE:
# There are no letters in one string to compare
#
# CASE 1:
# The last letter of P and Q are the same
#
# CASE 2:
# The last letter of P and Q are different
# """

from datetime import datetime


def LCS(P, Q, n, m):
    """

    :param P: str
    :param Q: str
    :param n: int
    :param m: int
    :return:
    """

    result = None
    keyy = f'{n-1},{m-1}'
    if keyy in matrix.keys():
        return matrix[keyy]

    # BASE CASE
    if n == 0 or m == 0:
        result = 0

    # CASE 1
    elif P[n-1] == Q[m-1]:
        result = 1 + LCS(P, Q, n-1, m-1)

    # CASE 2
    elif P[n-1] != Q[m-1]:
        tmp1 = LCS(P, Q, n-1, m)
        tmp2 = LCS(P, Q, n, m-1)
        result = max(tmp1, tmp2)

    matrix[f'{n-1},{m-1}'] = result
    return result


x = "ABCBDAB"
y = "BDCABA"

ans = ["BDAB", "BCAB", "BCBA"]

matrix = {}
start = datetime.now()
print(LCS(x, y, len(x), len(y)))
end = datetime.now()
delta = end-start
print(delta)
