with open('input.txt') as f:
    lines = f.read().splitlines()

maxCal = 0
sumCal = 0
secondMaxCal = 0
thirdMaxCal = 0
cal = []
for line in lines:
    if line != "":
        sumCal = sumCal + int(line)
    else:
        cal.append(sumCal)
        sumCal = 0

print(sorted(cal))
