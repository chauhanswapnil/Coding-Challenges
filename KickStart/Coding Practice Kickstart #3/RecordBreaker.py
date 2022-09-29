def solution(N,arr):
    currMax = arr[0]
    ans = 0
    # Check for the first day first
    if N==1 or (arr[0] > arr[1]):
        ans+=1
    for i in range(1,N):
        if arr[i] > currMax: # This means all previous numbers are also less than arr[i] so condition 1 satisfied
            currMax = arr[i]
            # Check for second condition or if its last number
            if i+1 == N:
                ans+=1
            else:
                if arr[i] > arr[i+1]:
                    ans+=1
    return ans

num_cases = int(input())
for case in range(1, num_cases + 1):    
    N = int(input())
    arr = [int(s) for s in input().split(" ")]
    ans = solution(N, arr)
    print('Case #{}: {}'.format(case, ans))