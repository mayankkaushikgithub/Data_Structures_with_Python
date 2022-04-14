# Replacing a Character with another

def replaceChar(s, a, b):

    if len(s) == 0:                 # Base Case
        return s
    # Hypothesis: our fun. can do this for l-1 sized string

    smallOutput = replaceChar(s[1:], a, b)         # strings are immutable so we need to create a new string every time
    # smallOutput stores all the replaced characters

    if s[0] == a:
        return b + smallOutput
    else:
        return s[0] + smallOutput


print(replaceChar("dacdxcd", 'c', 'x'))



