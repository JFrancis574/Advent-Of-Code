with open('input.txt', 'r') as file:
    data = file.read()
file.close()

splitData = data.split('\n')

outDict = {}
elfCount = 0
runningTotal = 0

for x in range(len(splitData)):
    if splitData[x] != '':
        print('Split: ', splitData[x])
        runningTotal += int(splitData[x])
    else:
        outDict[elfCount] = runningTotal
        elfCount += 1
        runningTotal = 0
        
outDict[elfCount] = runningTotal

finalValuesOrganised = sorted(outDict.values())
       
# Part 1 
print("Most calories: ", finalValuesOrganised[-1])

# Part 2
print("Total carried by top three: ", sum(finalValuesOrganised[-3:]))
        