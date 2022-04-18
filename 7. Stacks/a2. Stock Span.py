'''
Stock Span

Afzal has been working with an organization called 'Money Traders' for the past few years.
The organization is into the money trading business. His manager assigned him a task.
For a given array/list of stock's prices for N days, find the stock's span for each day.

The span of the stock's price today is defined as the maximum number of consecutive days
(starting from today and going backwards) for which the price of the stock was less than today's price.

For example, if the price of a stock over a period of 7 days are [100, 80, 60, 70, 60, 75, 85],
then the stock spans will be [1, 1, 1, 2, 1, 4, 6].

Explanation:
On the sixth day when the price of the stock was 75, the span came out to be 4,
because the last 4 prices(including the current price of 75) were less than the current or the sixth day's price.
Similarly, we can deduce the remaining results.
Afzal has to return an array/list of spans corresponding to each day's stock's price. Help him to achieve the task.

Input Format:
    The first line of input contains an integer N, denoting the total number of days.
    The second line of input contains the stock prices of each day. A single space will separate them.
Output Format:
    The only line of output will print the span for each day's stock price. A single space will separate them.

Note:   You are not required to print the expected output explicitly. It has already been taken care of.
Constraints:    0 <= N <= 10^7      1 <= X <= 10^9      Where X denotes the stock's price for a day.
Time Limit: 1 second

Sample Input 1:     4                                       Sample Output 1:    1 1 1 1
                    10 10 10 10
Sample Input 2:     8                                       Sample Output 2:    1 2 3 4 1 1 2 8
                    60 70 80 100 90 75 80 120
'''




from sys import stdin

def stockSpan(price, n) :       # this is without using STACK. Time Com. O(n^2)

    n = len(price)
    S = [None]*n
    S[0] = 1

    for i in range(1, n):
        S[i] = 1

        j = i - 1                   # to compare previous element

        while j >= 0 and price[i] > price[j]:
            S[i] += 1
            j -= 1

    return S




'''-------------- Utility Functions --------------'''

def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)

