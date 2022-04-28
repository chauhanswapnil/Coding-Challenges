# If more odds then convert evens
# if even number of odds then operations required are number of odds/2
# if equal even and odds then operations required are number of evens/odds / 2 
# if odd number of odds then operations is number of odds/2 + 1
def good(n,a):
    odd = 0
    even = 0
    for i in a:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    if even == 0 or odd == 0:
        return 0
    
    
    if odd % 2 == 0:    
        return min(even,odd // 2)
    else:
        return even
    # if even > odd:
    #     if odd % 2 == 0:
    #         return odd // 2
    #     else:
    #         return even
    # else:
    #     return even
        
num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    ans = str(good(n,a))
    print(ans)