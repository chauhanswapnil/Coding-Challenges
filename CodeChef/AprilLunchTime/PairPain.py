# def solution(arr, n):
#     ans = 0
#     for i in range(0, n):
#         j = i-1
#         while(j >= 0):
#             if (arr[i] + arr[j] >= arr[i] * arr[j]):
#                 ans = ans + 1
#             j = j - 1
#     return ans

# num_cases = int(input())
# for case in range(1, num_cases + 1):
#     n = int(input())
#     arr = [int(s) for s in input().split(" ")]
#     ans = solution(arr,n)
#     print(ans)
    
def solution(arr, n):
    count01 = 0
    count2 = 0
    for i in arr:
        if i == 0 or i == 1:
            count01 += 1
        if i == 2:
            count2 +=1
    ans = 0
    i = len(arr) - 1
    while count01 != 0:
        ans = ans + i
        i-=1
        count01 -=1
    
    count2 -= 1
    while count2 != 0:
        ans += count2
        count2 -= 1
        
    return ans

# num_cases = int(input())
# for case in range(1, num_cases + 1):
#     n = int(input())
#     arr = [int(s) for s in input().split(" ")]
#     ans = solution(arr,n)
#     print(ans)
    
    
    
def solution(arr,n):
    twoCount = 0
    twoGrCount = 0
    for i in range(0, n):
         
        if (arr[i] == 2):
            twoCount += 1
        elif (arr[i] > 2):
            twoGrCount += 1
     
    val = ((twoCount * twoGrCount) + (twoGrCount * (twoGrCount - 1)) // 2)
    total = ((n) * (n-1))//2
    
    return total-val