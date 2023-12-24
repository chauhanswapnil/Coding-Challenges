# [D]                     [N] [F]
# [H] [F]             [L] [J] [H]
# [R] [H]             [F] [V] [G] [H]
# [Z] [Q]         [Z] [W] [L] [J] [B]
# [S] [W] [H]     [B] [H] [D] [C] [M]
# [P] [R] [S] [G] [J] [J] [W] [Z] [V]
# [W] [B] [V] [F] [G] [T] [T] [T] [P]
# [Q] [V] [C] [H] [P] [Q] [Z] [D] [W]
#  1   2   3   4   5   6   7   8   9

stack = {
    1: ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'],
    2: ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
    3: ['C', 'V', 'S', 'H'],
    4: ['H', 'F', 'G'],
    5: ['P', 'G', 'J', 'B', 'Z'],
    6: ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
    7: ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'],
    8: ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
    9: ['W', 'P', 'V', 'M', 'B', 'H']
}


with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = []
for line in lines:
    line = line.split(" ")
    instructions.append([int(line[1]), int(line[3]), int(line[5])])

# stack = {
#     1: ["Z", "N"],
#     2: ["M", "C", "D"],
#     3: ["P"]
# }
# instructions = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]

for instruction in instructions:
    popCrate = instruction[1]
    pushCrate = instruction[2]
    numberOfMoves = instruction[0]
    # Popping from crate then pushing into crate
    popped = []
    for i in range(0, numberOfMoves):
        popped.append(stack[popCrate].pop())
    stack[pushCrate].extend(list(reversed(popped)))

print(stack)

ans = ""
for i in range(1, 10):
    ans += stack[i].pop()
print(ans)
