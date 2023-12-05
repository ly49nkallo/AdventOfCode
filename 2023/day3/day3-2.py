def main():
    with open('./input.txt', 'r') as f:
        contents = f.readlines()
        for i in range(len(contents)):
            contents[i] = contents[i][:-1]
    gears = dict()
    height = len(contents)
    width = len(contents[0])
    total = 0
    start = -1
    for i in range(height):
        line = contents[i]
        buf = ''
        for j in range(width):
            c = line[j]
            if c.isnumeric():
                if start == -1:
                   start = j 
                buf += c
            if (not c.isnumeric() and buf != '') or (j == width -1):
                if buf == '':
                    continue
                end = j
                if j == width -1:
                    end += 1
                num = int(buf)
                part = False
                already_found_gear = False
                # print()
                # print(num, start, end)
                for k in range(start, end):
                    for a in range(-1,2,1):
                        for b in range(-1,2,1):
                            if i + a >= height or k + b >= width or i + a < 0 or k + b < 0:
                                continue
                #            print(contents[i+a][k+b], end='')
                            if not (contents[i+a][k+b].isnumeric()) and not (contents[i+a][k+b] == '.'):
                                part = True
                                if contents[i+a][k+b] == '*' and not already_found_gear:
                                    already_found_gear = True
                                    if (i+a)*width + (k+b) not in gears:
                                        gears[(i+a)*width + (k+b)] = [{num},1]
                                    else:
                                        gears[(i+a)*width + (k+b)][0].add(num)
                                        gears[(i+a)*width + (k+b)][1] += 1

                # print(part)
                # print()
                if part:
                    # print('part', num)
                    total += num
                    num = 0
                start = -1

                buf = ''
    grs = [] 
    for gear in gears:
        gear_ratio = 1
        if gears[gear][1] != 2:
            continue
        zm = 0
        for num in gears[gear][0]:
            zm += 1
            gear_ratio *= num

        if gears[gear][1] == 2 and len(gears[gear][0]) == 1:
            gear_ratio = list(gears[gear][0])[0] ** 2
            zm = 2

        assert (zm == 2), f'too many numbers: {gears[gear]}'
        grs.append(gear_ratio)
    print(sum(grs))

main()

