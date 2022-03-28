'''
Google Kickstart 2022 Round - B
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7021
'''
def speedtyping(I,P):
    if len(P) < len(I):
        return -1
    C=0
    i = 0
    j = 0
    while (i < len(I) and j < len(P)):
        if I[i] == P[j]:
            i+=1
            j+=1
        else:
            j+=1
            C+=1
    if i == len(I):
        return (len(P) - len(I))
    else:
        return -1
    
num_cases = int(input())

for case in range(1, num_cases + 1):
    I = input()
    P = input()
    C = speedtyping(I, P)
    result = "IMPOSSIBLE" if C == -1 else C
    print('Case #{}: {}'.format(case, result))
    
# print(speedtyping("hello", "hiello"))
