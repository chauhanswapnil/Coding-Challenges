# graph = [ {"swap" : ["khush", "gala"]}, 
#         {"khush" : ["mop"]},
#         {"ram" : ["lax", "dam", "sam"]},
#         {"mop": ["drake"]}]

# def battles(graph):
#     for char in graph:
#         dfs(graph, list(char.keys())[0])

# def dfs(graph, source):
#     # print(source)
#     stack = [source]

#     while len(stack) > 0:
#         curr = stack.pop()
#         print(curr)
#         # if curr in graph.keys():
#         for neigh in graph[curr]:
#             stack.append(neigh)
#     return 1

# battles(graph)




'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. 
The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

               15
              / \
         14  13  21
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (15, 21), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9), (15, 13)
]

Write a function that takes this data and the identifiers of two individuals as inputs and 
returns true if and only if they share at least one ancestor. 

Sample input and output:

hasCommonAncestor(pairs, 3, 8)   => false
hasCommonAncestor(pairs, 5, 8)   => true
hasCommonAncestor(pairs, 6, 8)   => true
hasCommonAncestor(pairs, 6, 9)   => true
hasCommonAncestor(pairs, 1, 3)   => false
hasCommonAncestor(pairs, 3, 1)   => false
hasCommonAncestor(pairs, 7, 11)  => true
hasCommonAncestor(pairs, 6, 5)   => true
hasCommonAncestor(pairs, 5, 6)   => true
hasCommonAncestor(pairs, 3, 6)   => true
hasCommonAncestor(pairs, 21, 11) => true

n: number of pairs in the input
'''

pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (15, 21),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
    (15, 13)
]

'''

{
    3: [1,2],
    6: [3,5],
    7: [5],
    5: [4],
    21: [15],
    8: [4],
    9: [4,12],
    11: [9],
    4 : [14],
    12: [13],
    13: [15]
}

6-> 3,5,1,2,4,14
8-> 4,14

'''

# def hasCommonAncestor(pairs, ind1, ind2):
#     graph = {}
#     for p,c in pairs:
#         if c not in graph:
#             graph[c] = []
#         graph[c].append(p)
    
#     ancestors1 = getAncestor(graph, ind1, [])
#     ancestors2 = getAncestor(graph, ind2, [])

#     if len(list(set(ancestors1).intersection(ancestors2))) > 0:
#         return True
#     else:
#         return False

# def getAncestor(graph, ind, ancestors):
#     curr = ind
#     if curr not in graph:
#         return []
#     for children in graph[curr]:
#         ancestors.append(children)
#         getAncestor(graph, children, ancestors)
    
#     return ancestors


# print(hasCommonAncestor(pairs, 3, 8)) #   => false
# print(hasCommonAncestor(pairs, 5, 8))  # => true
# print(hasCommonAncestor(pairs, 6, 8) )  #=> true
# print(hasCommonAncestor(pairs, 6, 9) )  #=> true
# print(hasCommonAncestor(pairs, 1, 3)  ) #=> false
# print(hasCommonAncestor(pairs, 3, 1)   )#=> false
# print(hasCommonAncestor(pairs, 7, 11)  )#=> true
# print(hasCommonAncestor(pairs, 6, 5)   )#=> true
# print(hasCommonAncestor(pairs, 5, 6)   )#=> true
# print(hasCommonAncestor(pairs, 3, 6)   )#=> true
# print(hasCommonAncestor(pairs, 21, 11) )#=> true



def hasCommonAncestor(pairs, id1, id2):
    # Create a map from child to parent
    parents = {}
    for p, c in pairs:
        parents[c] = p

    # Traverse the ancestry tree of the first individual to find their ancestors
    ancestors1 = set()
    while id1 in parents:
        id1 = parents[id1]
        ancestors1.add(id1)

    # Traverse the ancestry tree of the second individual to find their ancestors
    ancestors2 = set()
    while id2 in parents:
        id2 = parents[id2]
        ancestors2.add(id2)

    # Return whether the two individuals have at least one common ancestor
    return len(ancestors1 & ancestors2) > 0


print(hasCommonAncestor(pairs, 3, 8)) #   => false
print(hasCommonAncestor(pairs, 5, 8))  # => true
print(hasCommonAncestor(pairs, 6, 8) )  #=> true
print(hasCommonAncestor(pairs, 6, 9) )  #=> true
print(hasCommonAncestor(pairs, 1, 3)  ) #=> false
print(hasCommonAncestor(pairs, 3, 1)   )#=> false
print(hasCommonAncestor(pairs, 7, 11)  )#=> true
print(hasCommonAncestor(pairs, 6, 5)   )#=> true
print(hasCommonAncestor(pairs, 5, 6)   )#=> true
print(hasCommonAncestor(pairs, 3, 6)   )#=> true
print(hasCommonAncestor(pairs, 21, 11) )#=> true

# def findNodesWithZeroAndOneParents(pairs):
#     ans = {}
#     for (_, child) in pairs:
#         ans[child] = []
                
#     for (parent, child) in pairs:
#         ans[child].append(parent)
        
#     childrenZeroParents = set()
#     childrenOneParent = set()
    
#     for (parent, child) in pairs:
#         if parent not in ans.keys():
#             childrenZeroParents.add(parent)
            
#     for val in ans:
#         if len(ans[val]) == 1:
#             childrenOneParent.add(val)
            
#     finalAns = [list(childrenZeroParents), list(childrenOneParent) ]
    
#     return finalAns

# print(findNodesWithZeroAndOneParents(pairs))
        

