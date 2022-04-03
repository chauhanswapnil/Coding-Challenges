'''
CodeJam 2022 Qualification Round
3D Printing

'''

# def printing(P1, P2, P3):

#     minC = min(P1[0],P2[0],P3[0])
#     minM = min(P1[1],P2[1],P3[1])
#     minY = min(P1[2],P2[2],P3[2])
#     minK = min(P1[3],P2[3],P3[3])
    
#     pos = minC + minM + minY + minK
#     if pos < 1000000:
#         return "IMPOSSIBLE"
    
#     rem = pos - 1000000
#     minArr = sorted(enumerate([minC, minM, minY, minK]), key=lambda x:x[1])
#     arr = []
#     if rem == 0:
#         arr = minArr
#     k = 0
#     while(rem != 0):
#         idx ,toRemove = minArr[k]
#         if rem > toRemove:
#             rem = rem - toRemove
#             arr.append((idx, 0))
#             k+=1
#         else:
#             arr.append((idx, toRemove - rem))
#             rem = 0
#             k+=1
#             while(k == len(minArr) - 1):
#                 arr.append(minArr[k])
#                 k+=1
    
#     arr = sorted(arr, key=lambda x:x[0])
#     return " ".join([str(v) for _,v in arr])

# num_cases = int(input())
# for case in range(1, num_cases + 1):
#     P1 = [int(s) for s in input().split(" ")]
#     P2 = [int(s) for s in input().split(" ")]
#     P3 = [int(s) for s in input().split(" ")]
    
#     ans = printing(P1, P2, P3)
#     print('Case #{}: {}'.format(case, ans))

# P1 = [768763,148041,178147,984173]
# P2 = [699508, 515362, 534729, 714381]
# P3 = [949704, 625054, 946212, 951187]

# P1 = [300000,200000,300000,500000]
# P2 = [300000, 200000, 500000, 300000]
# P3 = [300000, 500000, 300000, 200000]

# print(printing(P1, P2, P3))


def printing(P1, P2, P3):
    
    minC = min(P1[0],P2[0],P3[0])
    minM = min(P1[1],P2[1],P3[1])
    minY = min(P1[2],P2[2],P3[2])
    minK = min(P1[3],P2[3],P3[3])

    maxPos = minC + minM + minY + minK
    
    if maxPos == 1000000:
        return str(minC) + " " + str(minM) + " " + str(minY) + " " + str(minK)
    elif maxPos < 1000000:
        return "IMPOSSIBLE"
    else:
        maxPos = 0
        i = 0
        minArr = [minC, minM, minY, minK]
        while maxPos < 1000000:
            maxPos += minArr[i]
            i+=1
            if maxPos == 1000000:
                minArr2 = minArr[:i]
            else:
                minArr2 = minArr[:i-1]
                minArr2.append(1000000-sum(minArr[:i-1]))
            minArr2.extend(list(map(int,list('0'*(4-len(minArr2))))))
                
    return " ".join(str(v) for v in minArr2)

num_cases = int(input())
for case in range(1, num_cases + 1):
    P1 = [int(s) for s in input().split(" ")]
    P2 = [int(s) for s in input().split(" ")]
    P3 = [int(s) for s in input().split(" ")]
    ans = printing(P1, P2, P3)
    print('Case #{}: {}'.format(case, ans))

# P1 = [768763,148041,178147,984173]
# P2 = [699508, 515362, 534729, 714381]
# P3 = [949704, 625054, 946212, 951187]

# print(printing(P1, P2, P3))
