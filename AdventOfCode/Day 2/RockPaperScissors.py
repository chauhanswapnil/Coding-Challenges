with open('input.txt') as f:
    lines = f.read().splitlines()

strategy = []
for line in lines:
    line = line.split(" ")
    strategy.append([line[0], line[1]])

# strategy = [["A", "Y"], ["B", "X"], ["C", "Z"]]
# A Y
# B X
# C Z
totalScore = 0
for strat in strategy:
    opp, you = strat
    if (you == "X"):
        totalScore += 0
        if (opp == "A"):
            totalScore += 3
        if (opp == "B"):
            totalScore += 1
        if (opp == "C"):
            totalScore += 2
    if (you == "Y"):
        totalScore += 3
        if (opp == "A"):
            totalScore += 1
        if (opp == "B"):
            totalScore += 2
        if (opp == "C"):
            totalScore += 3
    if (you == "Z"):
        totalScore += 6
        if (opp == "A"):
            totalScore += 2
        if (opp == "B"):
            totalScore += 3
        if (opp == "C"):
            totalScore += 1

print(totalScore)
