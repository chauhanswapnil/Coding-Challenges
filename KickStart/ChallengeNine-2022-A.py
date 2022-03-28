'''

Google Kickstart 2022 Round - A 
Challenge Nine - Python
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997

'''

def challengeNine(N):
    num = str(N)
    c = len(num)
    ans = []
    for i in range(c+1):
        for j in range(0,10):
            if (i == 0 and j == 0) is False:
                num = num[:i] + str(j) + num[i:]
                if (int(num) % 9 == 0):
                    ans.append(int(num))
                num = str(N)
    return min(ans)
    
num_cases = int(input())
for case in range(1, num_cases + 1):
    N = input()
    ans = challengeNine(N)
    print('Case #{}: {}'.format(case, ans))
    
# print(challengeNine(12121))