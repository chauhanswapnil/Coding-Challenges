def solution(N, buses, P, cities):
    count = [0] * 5002
    for i in range(0,len(buses)):
        if i % 2 == 0:
            count[buses[i]] +=1
        else:
            count[buses[i] + 1] -= 1
    for i in range(1, len(count)):
        count[i] = count[i-1] + count[i]
    ans = []
    for city in cities:
        ans.append(count[city])
    return ' '.join(str(i) for i in ans)


# print(solution(4, [15,25,30,35,45,50,10,20], 2, [15,25]))

num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    buses = input().split()    
    buses = [int(b) for b in buses]
    # buses = [int(s) for s in input().split(" ")]
    P = int(input())
    cities = []
    for i in range(0,P):
        cities.append(int(input()))
    ans = solution(N, buses, P,cities)
    print('Case #{}: {}'.format(case, ans))
    if case != num_cases:
      _ = input()