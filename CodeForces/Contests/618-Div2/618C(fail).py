q = input()
numArray = [int(x) for x in input().split()]

numArray.sort(reverse=True)

for x in range(len(numArray)-1):
    if ((numArray[x] | numArray[x+1]) - numArray[x+1]) < ((numArray[x+1] | numArray[x]) - numArray[x]):
        temp = numArray[x + 1]
        numArray[x + 1] = numArray[x]
        numArray[x] = temp


start = numArray[0]
for x in range(len(numArray)-1):
    max = (start | numArray[x+1]) - numArray[x+1]
    for y in range(x+1, len(numArray)):
        if (start | numArray[y]) - numArray[y] > max:
            temp = numArray[x+1]
            numArray[x+1] = numArray[y]
            numArray[y] = temp
            max = (start | numArray[x+1]) - numArray[x+1]
    start = (start | numArray[x+1]) - numArray[x+1]

for x in range(len(numArray)-1):
    if ((numArray[x] | numArray[x+1]) - numArray[x+1]) < ((numArray[x+1] | numArray[x]) - numArray[x]):
        temp = numArray[x + 1]
        numArray[x + 1] = numArray[x]
        numArray[x] = temp

print(*numArray)
