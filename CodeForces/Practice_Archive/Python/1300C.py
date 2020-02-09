q = int(input())
numArray = [int(x) for x in input().split()]
binaryArray = ["{:030b}".format(x) for x in numArray]
max = 0
first = -1
for x in range(30):
    count = 0
    for y in range(q):
        if int(binaryArray[y][x]) == 1:
            count += 1
    if count == 1:
        for y in range(q):
            if int(binaryArray[y][x]) == 1:
                first = y
                break
    if first != -1:
        break

numArray[0], numArray[first] = numArray[first], numArray[0]
print(*numArray)