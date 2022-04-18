'''
Minimum bracket Reversal

For a given expression in the form of a string, find the minimum number of brackets that can be reversed
in order to make the expression balanced. The expression will only contain curly brackets.
If the expression can't be balanced, return -1.

Example:
Expression: {{{{
If we reverse the second and the fourth opening brackets, the whole expression will get balanced.
Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

Expression: {{{
In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket
and hence will not be able to make the expression balanced and the output will be -1.

Input Format :
        The first and the only line of input contains a string expression, without any spaces in between.
Output Format :
        The only line of output will print the number of reversals required to balance the whole expression.
        Prints -1, otherwise.

Note:   You don't have to print anything. It has already been taken care of.

Constraints:        0 <= N <= 10^6      Where N is the length of the expression.
Time Limit: 1sec

Sample Input 1:     {{{                 Sample Output 1:    -1

Sample Input 2:     {{{{}}              Sample Output 2:    1
'''




from sys import stdin

def countBracketReversals(inputString) :

    if len(inputString) % 2 != 0:                           # odd string can never be balanced
        return -1

    stack = []                                              # declare stack & count var globally
    count = 0
    for char in inputString:

        if char == '{':                                     # push every opening bracket in stack
            stack.append(char)

        elif char == '}':                                   #
            if len(stack) != 0:                             # if len(stack) is not 0

                if (stack[len(stack)-1] == '{'):
                    stack.pop(len(stack)-1)
                elif (stack[len(stack)-1] == '}'):
                    stack.append(char)

            else:
                stack.append(char)

    # for i in range(len(stack)):                       # for your convenience print the stack formed after push/pop
    #     print(stack[i], end=" ")

    while len(stack) != 0:

        c1 = stack[len(stack)-1]                            # insert top two elements in stack
        c2 = stack[len(stack)-2]
        # print(c1)
        # print(c2)

        if c1 == c2:                                        # if remaining ele are equal, they can form a pair
            stack.pop(len(stack)-1)                         # remove top two elements one by one from stack
            stack.pop(len(stack)-1)
            count += 1                                      # count them

        elif c1 != c2:                                      # when c1 & c2 both are different -> } {
            stack.pop(len(stack)-1)
            stack.pop(len(stack)-1)
            count += 2

    return count







#main
print("Enter the Expression: ")
print(countBracketReversals(stdin.readline().strip()))
