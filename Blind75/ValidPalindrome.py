import re
def isPalindrome(s):
    s = re.sub('[^A-Za-z0-9]+','',s)
    s = s.lower()
    newS = ''.join(c for c in reversed(s))
    return (s == newS)

print(isPalindrome("0P"))