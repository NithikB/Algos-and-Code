N = int(input())
for i in range(N):
    test_bool = True
    num_len = int(input())
    num = str(input())
    num_sum = sum([int(i) for i in num])

    if (int(num) % 2 == 1) and (num_sum % 2 == 0):
        print(int(num))
    elif (num_sum % 2 == 0) and int(num) % 2 == 0:
        for x in range(num_len-1, 1, -1):
            if int(num[x-1]) % 2 == 1:
                print(int(num[:x]))
                test_bool = False
                break
        if test_bool:
            print("-1")
    elif int(num) % 2 == 0:
        for x in range(num_len-1, 1, -1):
            if int(num[x-1]) % 2 == 1:
                num = num[:x]
                break
        if num_len != len(num):
            for x in range(len(num) - 1):
                if int(num[x]) % 2 == 1:
                    print(int(num.replace(num[x], '', 1)))
                    test_bool = False
                    break
        if test_bool:
            print("-1")
    else:
        for x in range(num_len-1):
            if int(num[x]) % 2 == 1:
                print(int(num.replace(num[x], '', 1)))
                test_bool = False
                break
        if test_bool:
            print("-1")