'''
Geometric Sum

Given k, find the geometric sum i.e.    1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k)     using recursion.

Input format :      Integer k
Output format :     Geometric sum (upto 5 decimal places)
Constraints :       0 <= k <= 1000

Sample Input 1 :    3               Sample Output 1 :   1.87500
Sample Input 2 :    4               Sample Output 2 :   1.93750
'''


# def geometricSum(num):              # without recursion
#     a = 1
#     for i in range(1, num+1):
#         a = a + 1/(2**i)
#     return format(a, '.5f')         # Add zeros to a float after the decimal point in Python


def geometricSum(num):                  # using recursion

    if num == 0:                        # Base Case
        return 1

    a = (1/(2**num) + float(geometricSum(num-1)))
    # convert to float otherwise it'll give TypeError: unsupported operand type(s) for +: 'float' and 'str'
    # return format((a), '.5f')
    return ('%.5f' % a)



print("Enter the Number:")
n = int(input())
res = geometricSum(n)
print(res)
