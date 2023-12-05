def main():
    # read file into memory
    powers = []
    with open('./input.txt', 'r') as f:
        file_contents = f.readlines()

    for i, line in enumerate(file_contents):
        # parse text
        data = parse_line(line)
        max_red = max([d[0] for d in data])
        max_green = max([d[1] for d in data])
        max_blue = max([d[2] for d in data])
        power = max_red * max_blue * max_green
        powers.append(power)

    print(sum(powers))

def parse_line(line) -> list[list]:
    ''' Returns a list of 3-lists (R,G,B) that represent each event'''
    ret = []
    i = 0

    while(line[i] != ':'):
        i += 1

    while i + 2 < len(line):
        i += 2
        event = [0] * 3
        while(i < len(line) and line[i] != ';'):
            buf = ''
            while(line[i].isnumeric()):
                buf += line[i]
                i += 1
            if buf != '':
                num = int(buf)
            buf = ''
            i += 1
            while(i < len(line) and line[i].isalpha()):
                buf += line[i]
                i += 1
            if buf == 'red':
                event[0] = num
            elif buf == 'green':
                event[1] = num
            elif buf == 'blue':
                event[2] = num
        ret.append(event)
    return ret

main()
