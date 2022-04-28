# There should be values before mex but no mex
# For mex 3 there should be 0,1 and 2 in the sequence
# If there is no number in the array that makes mex then infinite
# (0 - 1) = 0 so no number makes mex so infinite

def stable_mex(n,a):
    mex = smallestNonNegative(a)
    maxx = max(a)
    count = 0
    
    # if mex == 0:
    #     return 1
    
    
    
    for k in range(1,maxx):
        arr = []
        for i in a:
            arr.append(max(i-k,0))
        if smallestNonNegative(arr) == mex:
            count+=1
    if count == maxx:
        return -1
    else:
        return count    

def smallestNonNegative(A):
    if 0 not in A:
        return 0
    m = max(A)
    A = set(A)
    B = set(range(1, m + 1))
    D = B - A
    if len(D) == 0:
        return m + 1
    else:
        return min(D)
    
# num_cases = int(input())
# for case in range(1, num_cases + 1):
#     n = int(input())
#     a = [int(s) for s in input().split(" ")]
#     ans = str(stable_mex(n,a))
#     print(ans)
    
print(stable_mex(3,[0,1,100]))
# print(stable_mex(1,[0]))