with open('day1_inputs.txt', 'r') as file:
    elfCalsIn = file.read()
file.close()

splitLine = elfCalsIn.splitlines()

calorieCnt = 0
elfCalorieSums = []

# Part 1
for i in range (0, len(splitLine)):
    if splitLine[i] == "":
        elfCalorieSums.append(calorieCnt)
        calorieCnt = 0
    else:
        calorieCnt += int(splitLine[i])

print("Hungriest elf is: %d" %max(elfCalorieSums))

# Part 2
topCnt = 3
runningSum = 0
for i in range(topCnt):
    runningSum += max(elfCalorieSums)
    elfCalorieSums.remove(max(elfCalorieSums))

print("Sum of the three hungriest elves: %d" %runningSum)
