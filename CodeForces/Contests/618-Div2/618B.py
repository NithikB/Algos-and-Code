for jk in range(int(input())):
    q = int(input())
    numArray = [int(x) for x in input().split()]
    numArray.sort()
    print(numArray[q]-numArray[q-1])