numArray = [int(x) for x in input().split()]
sum1 = (numArray[0]|numArray[1]) - numArray[1]
for x in range(1, len(numArray)-1):
    sum1 = ((sum1|numArray[x+1]) - numArray[x+1])
print(sum1)