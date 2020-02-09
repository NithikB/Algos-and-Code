for i in range(int(input())):
    q = input()
    locations = {(0, 0): 1}
    x = 0
    y = 0
    first_index = -1
    last_index = 1
    min_sub_len = 200000
    min_sub = []
    path = input()
    for each in path:
        if each == 'L':
            x -= 1
        elif each == 'R':
            x += 1
        elif each == 'U':
            y += 1
        elif each == 'D':
            y -= 1
        if locations.get((x, y)) is None:
            locations[(x, y)] = last_index + 1
        else:
            first_index = locations.get((x, y))
            if (last_index - first_index) < min_sub_len:
                min_sub_len = (last_index - first_index)
                min_sub = [first_index, last_index]
            locations[(x, y)] = last_index + 1
        if (last_index - first_index) == 1:
            break
        last_index += 1
    if not min_sub:
        print("-1")
    else:
        print(min_sub[0], min_sub[1])