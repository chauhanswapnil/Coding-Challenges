'''

Palindrome Free Strings
Google Kickstart 2022 Round - C

100???001
Impossible

1000??
Possible

All Possible combinations of String is 2 ^ number of question marks.
For each possible combination get all its 5 length or more substrings check if it palindrome or not. 

'''

import itertools
# Brute Force Approach
def palindrome_free_strings_brute(N,S):
    ques_index = []
    k = 0
    for i in range(len(S)):
        if S[i] == "?":
            ques_index.append(i)
            k+=1
    
    for b in itertools.product([0, 1], repeat=k):
        possible_str = S
        for i in range(0, len(ques_index)):
            possible_str = possible_str[:ques_index[i]] + str(b[i]) + possible_str[ques_index[i]+1:]
            
        flag = 0
        for i in range(len(possible_str)):
            subStr = ""
            for j in range(i, len(possible_str)):
                subStr+=possible_str[j]
                if (len(subStr) >= 5 and checkPalindromeBrute(subStr)):
                    flag = 1
        if flag == 0:
            return True    
        
    return False

def checkPalindromeBrute(S):
    j = len(S) - 1
    for i in S:
        if i != S[j]:
            return False
        j-=1
    return True

# Taking Input
num_cases = int(input())
for case in range(1, num_cases + 1):
    N = input()
    S = input()
    ans = "POSSIBLE" if palindrome_free_strings_brute(N,S) else "IMPOSSIBLE"
    print('Case #{}: {}'.format(case, ans))
    
    
    

'''
Faster Approach
Tut: https://www.youtube.com/watch?v=TkP5ejvzfWI
Note: if length is even and it is palindrome then the middle 6 characters will be palindrome
if length is odd and it is palindrome then the middle 5 characters will be palindrome

Keep track of all current possibilities and if a new ? comes then put 1 and 0 and check if it becomes possible. 
If it does then make the new current possibility as the last 5 characters.


'''

def palindrome_free_strings(N,S):
    if N <=4 :
        return True
    q1 = []
    q2 = []
    if S[0] == "?":
        q1.append("0")
        q1.append("1")
    else:
        q1.append(S[0])
    flag = 0
    for i in range(1,N):
        while len(q1) != 0:
            front = q1.pop(0)
            if S[i] == '?':
                
                possibility = front + "0"
                if len(possibility) <=4:
                    q2.append(possibility)
                elif len(possibility) == 5:
                    if checkPalindrome(possibility) is False:
                        q2.append(possibility)
                else:
                    if checkPalindrome(possibility) is False and checkPalindrome(possibility[1:6]) is False:
                        q2.append(possibility[1:6])
                
                possibility = front + "1"
                if len(possibility) <=4:
                    q2.append(possibility)
                elif len(possibility) == 5:
                    if checkPalindrome(possibility) is False:
                        q2.append(possibility)
                else:
                    if checkPalindrome(possibility) is False and checkPalindrome(possibility[1:6]) is False:
                        q2.append(possibility[1:6])
            else:
                possibility = front + S[i]
                if len(possibility) <=4:
                    q2.append(possibility)
                elif len(possibility) == 5:
                    if checkPalindrome(possibility) is False:
                        q2.append(possibility)
                else:
                    if checkPalindrome(possibility) is False and checkPalindrome(possibility[1:6]) is False:
                        q2.append(possibility[1:6])
        
        while len(q2) != 0:
            q1.append(q2.pop(0))
        if len(q1) == 0:
            flag = 1
            break
    
    if flag == 0:
        return True
    else:
        return False
    
def checkPalindrome(S):
    if len(S) <= 4:
        return True
    j = len(S) - 1
    for i in S:
        if i != S[j]:
            return False
        j-=1
    return True

num_cases = int(input())
for case in range(1, num_cases + 1):
    N = input()
    S = input()
    ans = "POSSIBLE" if palindrome_free_strings(int(N),S) else "IMPOSSIBLE"
    print('Case #{}: {}'.format(case, ans))