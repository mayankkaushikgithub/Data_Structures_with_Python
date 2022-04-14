'''
Check Palindrome (recursive)
Send Feedback
Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S
Output Format :
'true' or 'false'
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
racecar
Sample Output 1:
true
Sample Input 2 :
ninja
Sample Output 2:
false
'''


## Read input as specified in the question.
## Print output as specified in the question.

def check_Palindrome_recursion(str):
    l = len(str)
    if l < 1:
        return True
    else:
        if str[0] == str[l - 1]:
            return check_Palindrome_recursion(str[1:l - 2])
        else:
            return False


# def check_Palindrome(str): 			# without using recursion
# 	for i in range(0, int(len(str)/2)): # Run loop from 0 to len/2,
# 		if str[i] != str[len(str)-i-1]: # comparing first element with last one
# 			return False
# 	return True


s = input()
# ans = check_Palindrome(s)
ans = check_Palindrome_recursion(s)

if (ans):
    print("true")
else:
    print("false")





