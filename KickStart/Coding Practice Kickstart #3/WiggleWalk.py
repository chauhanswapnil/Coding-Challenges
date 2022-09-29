# def solution(N,R,C, SR, SC, instructions):
#     matrix = [[0 for _ in range(C)] for _ in range(R)]
#     matrix[SR-1][SC-1] = 1
#     r, c = SR-1, SC-1
#     for ins in instructions:
#         while(True):
#             if ins == "N":
#                 r-=1
#             if ins == "S":
#                 r+=1
#             if ins == "E":
#                 c+=1
#             if ins == "W":
#                 c-=1
#             if matrix[r][c] == 1:
#                 continue
#             if matrix[r][c] == 0:
#                 matrix[r][c] = 1
#                 break
#     return (r+1,c+1)

# num_cases = int(input())
# for case in range(1, num_cases + 1):    
#     N, R, C, SR, SC = [int(s) for s in input().split(" ")]
#     instructions = input()
#     r, c = solution(N, R, C, SR, SC, instructions)
#     print('Case #{}: {} {}'.format(case, r, c))


# EFFICIENT MEMORY SOLUTION PASSED

# def solution(N,R,C, SR, SC, instructions):
#     r, c = SR-1, SC-1
#     visited = set()
#     visited.add(str((r,c)))
#     for ins in instructions:
#         while(True):
#             if ins == "N": 
#                 r-=1
#             if ins == "S":
#                 r+=1
#             if ins == "E":
#                 c+=1
#             if ins == "W":
#                 c-=1
#             if str((r,c)) in visited:
#                 continue
#             else:
#                 visited.add(str((r,c)))
#                 break
#     return (r+1,c+1)

# num_cases = int(input())
# for case in range(1, num_cases + 1):    
#     N, R, C, SR, SC = [int(s) for s in input().split(" ")]
#     instructions = input()
#     r, c = solution(N, R, C, SR, SC, instructions)
#     print('Case #{}: {} {}'.format(case, r, c))




# FASTER SOLUTION FOR BIGGER INPUTS
def solution(N,R,C, SR, SC, instructions):
    r, c = SR-1, SC-1
    visited = set()
    visited.add(str((r,c)))
    for ins in instructions:
        while(True):
            if ins == "N": 
                r-=1
            if ins == "S":
                r+=1
            if ins == "E":
                c+=1
            if ins == "W":
                c-=1
            if str((r,c)) in visited:
                continue
            else:
                visited.add(str((r,c)))
                break
    return (r+1,c+1)

num_cases = int(input())
for case in range(1, num_cases + 1):    
    N, R, C, SR, SC = [int(s) for s in input().split(" ")]
    instructions = input()
    r, c = solution(N, R, C, SR, SC, instructions)
    print('Case #{}: {} {}'.format(case, r, c))