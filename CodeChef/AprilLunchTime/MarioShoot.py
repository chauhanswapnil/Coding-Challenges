# def solution(x,y):
#     if x % 2 != 0 and y % 2 != 0:
#         return -1
#     palin1 = ""
#     palin2 = ""
#     if x%2 == 0 and y % 2 == 0:        
#         na = x//2
#         for i in range(na):
#             palin1 += "a"
#         for i in range(y):
#             palin1 += "b"
#         for i in range(na):
#             palin1 += "a"
    
#         nb = y//2
#         for i in range(nb):
#             palin2 += "b"
#         for i in range(x):
#             palin2 += "a"
#         for i in range(nb):
#             palin2 += "b"

#         return palin1,palin2
    
#     if x%2 != 0:
#         na = x // 2
#         for i in range(na):
#             palin1 += "a"
#         nb = y // 2
#         for i in range(nb):
#             palin1 += "b"
#         palin1 += "a"
#         for i in range(nb):
#             palin1 += "b"
#         for i in range(na):
#             palin1 += "a"
            
#         nb = y//2
#         for i in range(nb):
#             palin2 += "b"
#         for i in range(x):
#             palin2 += "a"
#         for i in range(nb):
#             palin2 += "b"
#     else:
#         na = x//2
#         for i in range(na):
#             palin1 += "a"
#         for i in range(y):
#             palin1 += "b"
#         for i in range(na):
#             palin1 += "a"
        
        
#         nb = y // 2
#         for i in range(nb):
#             palin2 += "b"
#         na = x // 2
#         for i in range(na):
#             palin2 += "a"
#         palin2 += "b"
#         for i in range(na):
#             palin2 += "a"
#         for i in range(nb):
#             palin2 += "b"
            
#     return palin1,palin2

# def solution(x,y):
#     if x % 2 == 0 and y % 2 == 0:
#         return ("a" * x//2 + "b" * y + "a" * x//2, 
#                 "b" * y//2 + "a" * x + "b" * y//2)        
#     elif x % 2 ==0:
#         return("a" * x//2 + "b" * y + "a" * x//2,
#                "b" * y//2 + "a" * x//2 + "b" + "a" * x//2 + "b" * y//2)
#     elif y % 2 == 0:
#         return ("b" * y//2 + "a" * x + "b" * y//2,
#                 "a" * x//2 + "b" * y//2 + "a" + "b" * y//2 + "a" * x//2)
#     else:
#         print(-1)

# num_cases = int(input())
# for case in range(1, num_cases + 1):
#     x,y = [int(s) for s in input().split(" ")]
#     ans = solution(x,y)
#     if ans == -1:
#         print(ans)
#     else:
#         a,b = ans
#         print(a)
#         print(b)

x = 4
print ("a" * (x//2) + "b" * 5)