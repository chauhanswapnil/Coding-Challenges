def solution(n,x):
    arr = []
    for i in range(n):
        arr.append(i)
    s = sum(arr) - arr[-1]
    valNeeded = (n*x) - s
    arr[-1] = valNeeded
    if arr[-1] > 1000 or arr[-1] < -1000:
        k = n - 2
        while arr[-1] < -1000 or arr[-1] > 1000:
            if arr[-1] < 1000:
                arr[-1] = arr[-1] + arr[k]
                arr[k] = 0
                k -= 1
            # if arr[-1] > 1000:
            #     arr[-1] = arr[-1] - arr[k]
            #     arr[k]
    print(sum(arr))
    return arr
    
# num_cases = int(input())
# for case in range(1, num_cases + 1):
#     n,x = [int(s) for s in input().split(" ")]
#     ans = solution(n,x)
#     joined_string = ' '.join([str(v) for v in ans])
#     print(joined_string)
    
print(solution(2,100))