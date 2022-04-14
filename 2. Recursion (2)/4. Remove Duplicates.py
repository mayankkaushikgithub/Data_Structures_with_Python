'''
Remove Duplicates Recursively

Given a string S, remove consecutive duplicates from it recursively.

Input Format :      String S
Output Format :     Output string
Constraints :       1 <= |S| <= 10^3        where |S| represents the length of string

Sample Input 1 :    aabccba             Sample Output 1 :   abcba
Sample Input 2 :    xxxyyyzwwzzz        Sample Output 2 :   xyzwz
'''

# Problem ID 91, removeConsecutiveDuplicates

# METHOD - 1      (using Recursion)
# 1. If string length is less than two (base case), there is nothing to compare, simply return the string
# 2. Otherwise (by induction) the string is at least two characters long.
#    If the first matches the second, drop the first letter and return the recursive result
# 3. Otherwise (by induction) the string is at least two characters long and the first two characters do not match.
#    Return the first char combined with the recursive result.

def removeConsecutiveDuplicates(string):

    if len(string) < 2:                              # Base Case: if nothing to compare return string
        return string

    # If the first matches the second, drop the first letter and return the recursive result
    if string[0] == string[1]:
        return removeConsecutiveDuplicates(string[1:])

    # If first two characters do not match. Return the first char combined with the recursive result.
    else:
        return string[0] + removeConsecutiveDuplicates(string[1:])
















# METHOD - 2    (without recursion)
# The idea is to keep track of two indexes, index of current character in str and
# index of next distinct character in str.
# Whenever we see same character, we only increment current character index.
# We see different character, we increment index of distinct character.
# def removeConsecutiveDuplicates(string):
#
#     i = 0       # index of current character
#     j = 0       # index of next distinct character in string
#     string = list(string)               # 'str' object does not support item assignment, so first convert it in list
#     for i in range(len(string)):        # traversing the string
#         if string[i] != string[j]:      # If current character S[i] is different from S[j]
#             j += 1                      # increase the j count by 1 as we don't want to change element at 0th index
#             string[j] = string[i]       # replace starts from 1st index not 0th
#     j += 1
#     string = string[0:j]
#     listToReturn = ' '.join(str(ele) for ele in string)
#     return listToReturn






# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
