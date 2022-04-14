# from sys import stdin
#
# def takeInput():
#     num = stdin.readline().rstrip().strip()
#     return int(num)
#
# def printNaturalNumbers_1_to_N(n):
#     if n == 0:
#         return
#     if n > 0:
#         printNaturalNumbers_1_to_N(n-1)            # first assume it'll print (n-1) nos. using PMI Hypothesis
#         print(n, end=" ")
#         return      # no need
#
# if __name__ == '__main__':
#     n = takeInput()
#     printNaturalNumbers_1_to_N(n)


# printing in reverse
from sys import stdin

def takeInput():
    num = stdin.readline().rstrip().strip()
    return int(num)

def printNaturalNumber_N_to_1(n):
    if n == 0:
        return
    print(n)
    printNaturalNumber_N_to_1(n-1)
    # pass

if __name__ == '__main__':
    n = takeInput()
    printNaturalNumber_N_to_1(n)
