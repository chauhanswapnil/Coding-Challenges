'''

CodeJam 2022 Qualification Round 
Punched Cards

'''


def punchedCards(R, C):
    R_len = R * 2 + 1
    C_len = C * 2 + 1
    arr = []
    for i in range(0, R_len):
        prtStr = ""
        for j in range(0, C_len):
            if (i == 0 and j == 0) or (i == 0 and j == 1) or (i == 1 and j == 0) or (i == 1 and j == 1):
                prtStr += "."
            else:
                if (i % 2 == 0 and j % 2 == 0):
                    prtStr += "+"
                elif (i % 2 != 0 and j % 2 != 0):
                    prtStr += "."
                elif (i % 2 == 0 and j % 2 != 0):
                    prtStr += "-"
                else:
                    prtStr += "|"
        arr.append(prtStr)
    return arr

num_cases = int(input())
for case in range(1, num_cases + 1):
    R, C = [int(s) for s in input().split(" ")]
    ans = punchedCards(R, C)
    print('Case #{}:'.format(case))
    for s in ans:
        print(s)