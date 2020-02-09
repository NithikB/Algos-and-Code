for jk in range(int(input())):
    q = input()
    numArray = [int(x) for x in input().split()]
    sumArray = sum(numArray)
    steps = numArray.count(0)
    sumArray += steps
    if sumArray == 0:
        steps += 1
    print(steps)