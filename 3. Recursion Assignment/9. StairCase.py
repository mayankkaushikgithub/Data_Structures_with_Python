'''
Staircase

A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time.
Implement a method to count how many possible ways the child can run up to the stairs.
You need to return number of possible ways W.

Input format :      Integer N
Output Format :     Integer W
Constraints :       1 <= N <= 30

Sample Input 1 :    4           Sample Output 1 :   7

Sample Input 2 :    5           Sample Output 2 :   13

'''

'''
Solution: RECURSION METHOD
If a person is standing at i-th stair, the person can move to i+1, i+2, i+3-th stair. 
A recursive function can be formed where at current index i the function is recursively called for i+1, i+2 and i+3th stair. 

There is another way of forming the recursive function. 
To reach a stair i, a person has to jump either from i-1, i-2 or i-3 th stair or i is the starting stair.

Algorithm: 

1. Create a recursive function (count(int n)) which takes only one parameter.
2. Check the base cases. If the value of n is less than 0 then return 0, and 
    if the value of n is equal to zero then return 1 as it is the starting stair.
3. Call the function recursively with values n-1, n-2 and n-3 and sum up the values that are returned, 
    i.e. sum = count(n-1) + count(n-2) + count(n-3)
    Return the value of the sum.
'''

def count(n):

    if n < 0:
        return 0

    if n == 0 or n == 1:
        return 1 # it is starting stair only 1 step is needed to climb 1 stair

    elif n == 2:
        return 2 # only 2 steps are needed to climb 2 Stairs

    else:
        sum = count(n-1) + count(n-2) + count(n-3)

    return sum
    # pass

print("Enter the Number of Stairs:")
num = int(input())

print("\nTotal Steps required:")
print(count(num))

