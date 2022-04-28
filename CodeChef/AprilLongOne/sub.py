def sub(n,m,s,a):
    setS = ["a","b","c","d","e"]
    # Find subsequence
    if findSub(s,a):
        return -1
    
    for i in setS:
        ns = s.replace("?", i)
        if findSub(ns,a) == False:
            return ns
    
    return s.replace("?", "e")

def findSub(s,a):
    current_pos = 0
    for c in a:
        current_pos = s.find(c, current_pos) + 1
        if current_pos == 0:
            return False
    return True
# print(sub(4,2,"a??", "ab"))
        
num_cases = int(input())
for case in range(1, num_cases + 1):
    n,m = [int(s) for s in input().split(" ")]
    s = input()
    a = input()
    ans = str(sub(n,m,s,a))
    print(ans)