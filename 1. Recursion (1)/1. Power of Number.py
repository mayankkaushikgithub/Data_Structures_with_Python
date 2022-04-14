'''
Power Of A Number

Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.

Note : For this question, you can assume that 0 raised to the power of 0 is 1

Input format :      Two integers x and n (separated by space)
Output Format :     x^n (i.e. x raise to the power n)
Constraints:        0 <= x <= 8         0 <= n <= 9

Sample Input 1 :    3 4             Sample Output 1 :   81
Sample Input 2 :    2 5             Sample Output 2 :   32
'''

from sys import stdin

def takeInput():
    print("Enter the Base Number & Power Factor up to which you want it to be raised:")
    li = stdin.readline().rstrip().split()
    x = int(li[0])
    n = int(li[1])

    return x, n

def powerOfNumber(x,n):
    if n != 0:
        return x * powerOfNumber(x, n-1)        # calling function recursively
    else:
        return 1


if __name__ == '__main__':

    x, n = takeInput()
    r = powerOfNumber(x, n)
    print(r)
