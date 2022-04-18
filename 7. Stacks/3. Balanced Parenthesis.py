'''
Balanced Parenthesis

For a given a string expression containing only round brackets or parentheses, check if they are balanced or not.
Brackets are said to be balanced if the bracket which opens last, closes first.

Example:    Expression: (()())
Since all the opening brackets have their corresponding closing brackets, we say it is balanced and
hence the output will be, 'true'.
You need to return a boolean value indicating whether the expression is balanced or not.
Note:   The input expression will not contain spaces in between.

Input Format:
    The first and the only line of input contains a string expression without any spaces in between.
Output Format:
    The only line of output prints 'true' or 'false'.

Note:   You don't have to print anything explicitly. It has been taken care of. Just implement the function.
Constraints:    1 <= N <= 10^7   Where N is the length of the expression.
Time Limit: 1sec

Sample Input 1 :        (()()())                Sample Output 1 :       true

Sample Input 2 :        ()()(()                 Sample Output 2 :       false

Explanation to Sample Input 2:
The initial two pairs of brackets are balanced. But when you see, the opening bracket at the fourth index doesn't
have its corresponding closing bracket which makes it imbalanced and in turn, making the whole expression imbalanced.
Hence the output prints 'false'.

'''

from sys import stdin


def isBalanced(expression):                     # Function to test balanced brackets stack for storing opening brackets

    stack = []

    for char in expression:                                     # Loop for checking each char in string

        if char == '{' or char == '(' or char == '[':           # if its opening bracket, so push it in the stack
            stack.append(char)

        # else if its closing bracket then check if the stack is empty then return false or
        # pop the top most element from the stack and compare it
        elif char == '}' or char == ')' or char == ']':

            if len(stack) == 0:                                 # this means we don't have a opening bracket
                return False

            top_element = stack.pop()  # pop
            if not Compare(top_element, char):
                return False

    if len(stack) != 0:                                         # lastly, check that stack is empty or not
        return False

    return True

def Compare(opening, closing):                                  # Check if two corresponding brackets equal or not.
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    return False





# main
print("Enter the Expression")
expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")

else:
    print("false")
