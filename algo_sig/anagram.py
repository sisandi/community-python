"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = “anagram”, t = “nagaram”
Output = true

Example 2:
Input: s = “rat”, t = “car”
Output = False

Assume string contains only lowercase letters

"""


def count_letters(s1):
    letters = {}

    for x in s1:
        if x in letters.keys():
            letters[x] += 1
        else:
            letters[x] = 1

    return letters


def isAnagram(s, t):

    result = True

    if len(s) != len(t):
        return False
    if s == t:
        return True

    lc_1 = count_letters(s)
    lc_2 = count_letters(t)

    for x in s:
        if x in t:
            print(x)
            if lc_1[x] != lc_2[x]:
                result = False
        else:
            return False

    return result


print(isAnagram("anagram", "angaarm"))










