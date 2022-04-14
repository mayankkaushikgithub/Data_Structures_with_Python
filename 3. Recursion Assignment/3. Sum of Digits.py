'''
Sum of digits (recursive)

Write a recursive function that returns the sum of the digits of a given integer.

Input format :      Integer N
Output format :     Sum of digits of N

Constraints :       0 <= N <= 10^9

Sample Input 1 :    12345       Sample Output 1 :   15
Sample Input 2 :    9           Sample Output 2 :   9
'''



def sumOfDigits(num):
    if num == 0:  # Base Case if no number is provided, return 0
        return 0

    else:
        # return right-most-digit along with rest of the digits of number
        return (num % 10) + (sumOfDigits(num // 10))


# def sumOfDigits(num): # without using recursion
#     sum = 0
#     while num > 0:		# run till no. is not 0
#         r = num % 10	# get right most digit of number
#         sum = sum + r	# add right most digit to sum
#         num = num//10	# divide the no. to take rest of the digits except r
#     return sum


n = int(input())
print(sumOfDigits(n))

