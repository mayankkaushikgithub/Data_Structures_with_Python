'''
Check redundant brackets

For a given expression in the form of a string, find if there exist any redundant brackets or not.
It is given that the expression contains only rounded brackets or parenthesis and the input expression
will always be balanced.
A pair of the bracket is said to be redundant when a sub-expression is surrounded by unnecessary or
 needless brackets.
Example:    Expression: (a+b)+c
Since there are no needless brackets, hence, the output must be 'false'.

Expression: ((a+b))
The expression can be reduced to (a+b). Hence the expression has redundant brackets and the output will be 'true'.

Input Format :
    The first and the only line of input contains a string expression, without any spaces in between.
Output Format :
    The first and the only line of output will print either 'true' or 'false'(without the quotes)
    denoting whether the input expression contains redundant brackets or not.

Note:   You are not required to print the expected result. It has already been taken care of.
Constraints:    0 <= N <= 10^6      Where N is the length of the expression.
Time Limit: 1 second

Sample Input 1:     a+(b)+c
Sample Output 1:    true
Explanation:    The expression can be reduced to a+b+c. Hence, the brackets are redundant.

Sample Input 2:     (a+b)
Sample Output 2:    false
'''



from sys import stdin

def checkRedundantBrackets(expression) :

	if len(expression) <= 3:						# if exp. is this short it won't have any in-significant characters
		# print(len(expression))
		return True

	stack = []										# take an empty stack

	for c in expression:							# traverse the input expression

		if c != ')':								# push all characters in stack from start, except ')'
			stack.append(c)

		else:										# if the current char in the expression is a closing parenthesis

			if stack[len(stack)-1] == '(':			# if (after removing all ele), 'top' ele is '(' then return true
				return True

			while stack[-1] != '(':					# pop till `(` is found for current `)`
				stack.pop()

			stack.pop()											# pop last `(`, empty the stack

	return False						# if we reach here, then the expression doesn't have any duplicate parenthesis







#main
print("Enter the Expression: ")
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
