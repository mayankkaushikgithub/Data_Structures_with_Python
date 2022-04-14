'''
Check AB

Suppose you have a string, S, made up of only 'a's and 'b's.
Write a recursive function that checks if the string was generated using the following rules:
    a. The string begins with an 'a'
    b. Each 'a' is followed by nothing or an 'a' or "bb"
    c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.

Input format :      String S
Output format :     'true' or 'false'
Constraints :       0 <= |S| <= 1000        where |S| represents length of string S.

Sample Input 1 :    abb             Sample Output 1 :   true

Sample Input 2 :    abababa         Sample Output 2 :   false

'''

def checkAB(str, flag, bflag):

    if len(str) == 0:
        return flag

    elif str[0] == "a":
        flag = True
        bflag = False
        return checkAB(str[1:], flag, bflag)

    elif str[0] == "b" and str[1] == "b":
        if bflag == True:
            return False
        else:
            bflag = True
            return checkAB(str[2:], flag, bflag)

    else:
        return False


if __name__ == '__main__':

    str = input()
    flag = True
    bflag = False

    if str[0] == "a":                   # the given string must begin with 'a'
        x = checkAB(str, flag, bflag)
    else:                               # otherwise return 0
        x = 0

    if x:
        print("true")
    else:
        print("false")








