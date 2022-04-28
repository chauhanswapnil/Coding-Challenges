count = 0
def cupcakeDP(n, memo):
    if n in memo:
        # print(n)
        return memo[n]
    if n==0:
        return True
    if n<0:
        return False
    # print(memo)
    # print(n)
    memo[n] = cupcakeDP(n-4,memo) or cupcakeDP(n-6,memo) or cupcakeDP(n-9,memo)
    
    # memo[n-4] = cupcakeDP(n-4,memo)
    # memo[n-6] = cupcakeDP(n-6,memo)
    # memo[n-9] = cupcakeDP(n-9,memo)
    # return memo[n-4] or memo[n-6] or memo[n-9]
    return memo[n]
    
    

def cupcake(n):
    if n==0:
        return True
    if n<0:
        return False
    return cupcake(n-4) or cupcake(n-6) or cupcake(n-9)

print(cupcakeDP(11,{}))         
# print(cupcake(1234))



# from Measure import measure
# measure(cupcakeDP,690,{})
# measure(cupcake,690)
