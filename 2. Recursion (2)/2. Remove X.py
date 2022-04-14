'''
Remove X

Given a string, compute recursively a new string where all 'x' chars have been removed.
Input format :      String S
Output format :     Modified String
Constraints :       1 <= |S| <= 10^3        where |S| represents the length of string S.

Sample Input 1 :    xaxb            Sample Output 1:    ab

Sample Input 2 :    abc             Sample Output 2:    abc

Sample Input 3 :    xx              Sample Output 3:
'''



# Problem: Remove x from string
# def removeX(string):                        # without using recursion
#     if len(string) == 0:
#         return string
#     else:
#         return string.replace('x', '')

def removeX(string, X):                            # using recursion

# Base Case:  If the length of the string str called recursively is 0 then return the empty string from the function
    if len(string) == 0:
        return ""


# Recursive Call: If the base case is not met, then check for the character at 0th index
# if it is X then recursively iterate for the substring removing the first character.
    if string[0] == X:
        return removeX(string[1:], X) # Pass the rest of the string to recursion Function call


# Return Statement: At each recursive call(except the base case and the above condition),
# return the recursive function for the next iteration including the character at 0th index.
    else:
        return string[0] + removeX(string[1:], X) # Add the first character of str and string from recursion




# Main
string = input()
# print(removeX(string))

X ='x'
res = removeX(string, X)
print(res)
