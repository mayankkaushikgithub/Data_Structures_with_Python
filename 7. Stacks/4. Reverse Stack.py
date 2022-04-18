'''
Reverse Stack

You have been given two stacks that can store integers as the data.
Out of the two given stacks, one is populated and the other one is empty.
You are required to write a function that reverses the populated stack using the one which is empty.

Input Format :
    The first line of input contains an integer N, denoting the total number of elements in the stack.
    The second line of input contains N integers separated by a single space, representing the order
    in which the elements are pushed into the stack.
Output Format:
    The only line of output prints the order in which the stack elements are popped, all of them separated
    by a single space.

Note:   You are not required to print the expected output explicitly, it has already been taken care of.
        Just make the changes in the input stack itself.
Constraints:        1 <= N <= 10^3      -2^31 <= data <= 2^31 - 1
Time Limit: 1sec

Sample Input 1: 6                                                         Sample Output 1:    1 2 3 4 5 10
                1 2 3 4 5 10
                Note: Here, 10 is at the top of the stack.                Note: Here, 1 is at the top of the stack.


Sample Input 2: 5                                                         Sample Output 2:    2 8 15 1 10
                2 8 15 1 10
'''




from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack) :

	if len(inputStack) <= 1:		# when we're at end return
		return

	while len(inputStack) != 1:		# put n-1 elements of 'inputstack' to 'extraStack'
		ele = inputStack.pop()
		extraStack.append(ele)

	lastElement = inputStack.pop() # store last element of stack somewhere else

	while len(extraStack) != 0:		# move each ele of extraStack to inputStack
		ele = extraStack.pop()
		inputStack.append(ele)

	reverseStack(inputStack, extraStack)	# call recursion on rest of the elements

	inputStack.append(lastElement)		# attach last element at the top of original stack

    # pass
	#Your code goes here







'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")