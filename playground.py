# def danceScore(scores, wait, k, skipTotal, chooseTotal):
#     if (k == len(scores) - 1):
#         print("Scores last", scores[k])
#         return scores[k] # Selecting
    
#     if (k+wait[k]+1 > len(scores) - 1):
#         print("Can't go further", scores[k])
#         return scores[k] # Selecting

#     skipTotal = skipTotal + danceScore(scores, wait, k+1, skipTotal, chooseTotal)
    
#     chooseTotal = chooseTotal + danceScore(scores,wait, k+wait[k]+1, skipTotal, chooseTotal)
    
#     print(skipTotal, chooseTotal)
#     return max(skipTotal, chooseTotal)

# def danceScore(scores, wait, k):
#     if k > len(scores) - 1:
#         return 0
    
#     dtotal = 0
#     stotal = 0
#     dtotal = max(dtotal, scores[k] + danceScore(scores, wait, k+1))

#     stotal = max(stotal, scores[k] + danceScore(scores, wait, k+wait[k]+1))
    
#     # chooseTotal = chooseTotal + danceScore(scores,wait, k+wait[k]+1, skipTotal, chooseTotal)
    
#     # print(skipTotal, chooseTotal)
#     return min(dtotal,stotal)


# print(danceScore([7,1,5,3,30],[3,0,1,2,3],0))
# # 7    

# class Time:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def printXY(self):
#         return ("Time (" + str(self.x) + "," + str(self.y) + ")")
# def solution():
#     dict = {0:[238,159], 
#             7:[290,311,8], 
#             67:[135, 173, 69, 68, 70, 71]}
    
#     newDict = {}
    
#     for key, value in dict.items():
#         tempDict = {}
#         for v in value:
#             tempDict[v] = Time(key,v)
#         newDict[key] = tempDict
    
#     for key,value in newDict.items():
#         print("For key = " + str(key))
#         for k,v in value.items():
#             print(str(k) + ":"+ v.printXY())
#         print ("")
# solution()


# def fibonacci(Number):
#     if(Number == 0):
#         return 0
#     elif Number == 1:
#         return 1
#     else:
#         return fibonacci(Number - 2) + fibonacci(Number - 1)

# N = 0
# Sum = 0
# i = 0
# while(N<10):
#     if(fibonacci(i)%2 == 0):
#         Sum = Sum + fibonacci(i)
#         N +=1
#     i +=1

# print(Sum)

# 1 1 2 3 5 8 11 .....
# def printFibonacciNumbers():
#     prev = 1
#     curr = 1
#     k = 1
#     sumFib = 0
#     while (k != 1000):
#         temp = curr
#         curr = prev + curr
#         prev = temp
#         if curr % 2 == 0:
#             sumFib+=curr
#             k+=1
#     print(sumFib)
# # Driven code
# printFibonacciNumbers()

# from itertools import combinations
# def solution(pattern, s):
#     c = 0
#     allSubStrs = [s[a:b] for a,b in combinations(range(len(s) + 1),r=2) if len(s[a:b]) == len(pattern)]
    
#     for value in allSubStrs:
#         flag = 0
#         for i in range(0,len(pattern)):
#             if (pattern[i] == "0" and 
#             (value[i] != "a" and 
#             value[i] != "e" and 
#             value[i] != "i" and 
#             value[i] != "o" and 
#             value[i] != "u" and 
#             value[i] != "y")):
#                 flag = 1
            
#             elif (pattern[i] == "1" and 
#             (value[i] == "a" and 
#             value[i] == "e" and 
#             value[i] == "i" and 
#             value[i] == "o" and 
#             value[i] == "u" and 
#             value[i] == "y")):
#                 flag = 1
#             if flag == 0:
#                 c+=1
#     return c
             


# from itertools import combinations

# def solution(pattern, s):
    
#     c = 0
#     allSubStrs = [s[a:b] for a, b in combinations(range(len(s) + 1), r = 2) if len(s[a:b]) == len(pattern)]

#     for value in allSubStrs:
#         flag = 0
#         for i in range(0,len(pattern)):
#             if pattern[i] == "0" and (value[i] != "a" and value[i] != "e" and value[i] != "i" and value[i] != "o" and value[i] != "u" and value[i] != "y"):
#                 flag = 1
#             elif pattern[i] == "1" and (value[i] == "a" or value[i] == "e" or value[i] == "i" or value[i] == "o" or value[i] == "u" and value[i] == "y"):
#                 flag = 1
#         if flag == 0:
#             c+=1
    
#     return c
    
# print(solution("1","xurjzrtjjicjkddqfvjjcqywlvznduzlfeinpjomrikwnjzrvkdqyrokxulxiunlppisblfgsvbflneifnwlnvfbcirzsbtnwzovoewlpmvlzwhwobshjjrhhjqovlayrxwuqaqwepmvmjanlfjdjtidyqjmpyqdtllicpcshghjltamcselirfhutmnahogqjthdfqcnztugpsebqnfkrywlashzipufskmrjwuhuqwotieuaugxdtedxmqsllpsubmhonrvgefvrnlnqhzknsvainapzacmtuidnhozdhksvxikohgyagjykgbyhzpzcgvgyikafavkkhtfylqcesiwcthqsobwbnzzsmrvliajtkxccyqbnxduzrfwnvnlyomczhcfovicyflmmicogsvmcghbsazyvlcquijjrleicaqadgnmpnjekphemjvbdbdbhpuibduacfecqnjsfuibdiygkvtcppyvwwfsjyzsyexgbudqyxgerkftlfjbsjayhwpuxrzdpumhrlpwvtlxacbdjbxvjedpfxmcmeigkytvwqgyyqklzuilphaesbtlqjoycuxcuzsdqcxagxqkyhphkxbbplpyoxtzkvuwkoolvyqzzxtinovgskstkvxmerjfgpvxxrqibgoavfczqdrikfxhagwefyshaypbqafbgqonhvbuqcdppxyperzesptxrpzrzdjelyrtkkkblhxcoigmbllswiefhhejiamzifznkojwbfpbuzneoqfdjtcuqrakvcfiolzcthjtqnvchdwkrnpongqnajkugccnolukpxmhvjjgbmsuajghwizyfttilddqjdseposcaxnmhvavdihqtsrrmafcpfrmwiublyqysthhvxskelqknosksttsktadqyuqfjaqbbjrarxpvbrhppkdeklqzzhwkrauqlyredxjwizeeatpgwzkeuikcpxlsirhvwwtgzchnxoxotfpycd"))


# def solution(matrix, i ,j , arr):
    
#     if i > len(matrix) or j > len(matrix[0]):
#         return arr
    
#     numRows = len(matrix)
#     numCols = len(matrix[0])
#     sum = 0;
#     for ii in range(0,numRows):
#         for jj in range(0, numCols):
#             if (ii == i or jj == j or ii == numRows - 1  or jj == numCols - 1):
#                 sum += matrix[ii][jj]
#     arr.append(sum)
#     print(arr)
#     solution(matrix, i+1, j+1, arr)


# def finalSolution (matrix):
#     return solution(matrix, 0,0, len(matrix), len(matrix[0]))

# def solution(matrix, i, j, m, n, ans = []):
    
#     sum = 0

#     if (i >= m or j >= n):
#         return
 
#     for p in range(i, n):
#         sum += matrix[i][p]
 
#     for p in range(i + 1, m):
#         sum += matrix[p][n-1]
 
#     if ((m - 1) != i):
#         for p in range(n - 2, j - 1, -1):
#             sum += matrix[m-1][p]
 
#     if ((n - 1) != j):
#         for p in range(m - 2, i, -1):
#             sum += matrix[p][j]
    
#     ans.append(sum)
#     solution(matrix, i + 1, j + 1, m - 1, n - 1,ans)
    
#     return ans
 
 
# # Driver code
# R = 4
# C = 4
# arr = [[1,2,2,3],
#                 [0,1,0,2],
#                 [4,-1,-1,-3],
#                 [4,-1,-1,3]
#                 ]
 
# # Function Call
# print(solution(arr, 0, 0, R, C))
 
print('\n'.join
 ([''.join
   ([('SwapKhus'[(x-y)%8 ]
     if((x*0.05)**2+(y*0.1)**2-1)
      **3-(x*0.05)**2*(y*0.1)
       **3<=0 else' ')
        for x in range(-30,30)])
         for y in range(15,-15,-1)]))
    
        
