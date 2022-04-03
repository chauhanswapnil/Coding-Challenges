'''
Code Jam Qualification Round 2022
Chain Reactions
'''

import itertools
def chainReactions(N, F, P):    
    graph = {}
    for i in range(N):
        if (i+1,F[i]) not in graph:
            graph[(i+1,F[i])] = []
        if P[i] != 0:
            graph[(i+1,F[i])].append((P[i], F[P[i]-1]))

    sources = []
    keys = []
    vals = []
    for key, val in graph.items():
        keys.append(key)
        if len(val) != 0:
            vals.append(val[0])
    for v in keys:
        if v not in vals:
            sources.append(v)
    
    totalFunMax = 0
    visited = set()
    
    i = 0
    for srcs in list(itertools.permutations(sources, len(sources))):
        
        totalFun = 0
        visited = set()
        for source in list(srcs):
            fun, visited = depthFirstPrint(graph, source,visited)
            totalFun+=fun
        if totalFun > totalFunMax:
            totalFunMax = totalFun

    # for source in sources:
    #     sourcesSorted.append((source, depthOfTraverse(graph,source)))
    # sourcesSorted = sorted(sourcesSorted, key=lambda x: (x[1],x[0][1]))

    # print(sourcesSorted)
        
    return totalFunMax

def depthOfTraverse(graph, source):
    stack = [source]
    fun = []
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        fun.append(curr[1])
        visited.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                stack.append(neighbor)
    return len(fun)

def depthFirstPrint(graph, source, visited):
    stack = [source]
    fun = []
    while len(stack) > 0:
        curr = stack.pop()
        fun.append(curr[1])
        visited.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                stack.append(neighbor)
    return (max(fun),visited)

num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    F = [int(s) for s in input().split(" ")]
    P = [int(s) for s in input().split(" ")]
    ans = chainReactions(N,F,P)
    print('Case #{}: {}'.format(case, str(ans)))

# N = 5
# F = [100,200,300,400,500]
# P = [2, 1,1, 1, 1]
# N = 8
# F = [100, 100, 100, 90, 80, 100, 90, 100]
# P = [0,1,2,1,2,3,1,3]
# N = 5
# F = [3,2,1,4,5]
# P = [0,1,1,1,0]

# N = 4
# F = [60,20,70,50]
# P = [0,1,1,2]

# print(chainReactions(N,F,P))