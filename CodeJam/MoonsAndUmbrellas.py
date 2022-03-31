'''
Moons and Umbrellas
Whenever we encounter a ? check its left and right.
If right is "?" go more right until you find J or C

'''

def moonsAndUmbrellas(X,Y, S):
    newStr = S.replace('?','')
    return (newStr.count('CJ') * X + newStr.count('JC') * Y)


num_cases = int(input())
for case in range(1, num_cases + 1):
    X, Y, S = [s for s in input().split(" ")]
    ans = moonsAndUmbrellas(int(X), int(Y), S)
    print('Case #{}: {}'.format(case, str(ans)))
    
    
# print(moonsAndUmbrellas(4,2, "CJCJ"))