def main():
    with open('./input.txt', 'r') as f:
        contents = f.readlines()
        for i in range(len(contents)):
            contents[i] = contents[i][:-1]
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
                # print(part)
                # print()
                if part:
                    # print('part', num)
                    total += num
                    num = 0
                start = -1

                buf = ''
                                
    print(total)

main()

