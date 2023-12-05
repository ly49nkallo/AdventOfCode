from pprint import pprint

def main():
    data = load_card_info()
    # pprint(data)
    l_total_points = []
    for card in data:
        
        u = card[0].intersection(card[1])
        points = 2 ** (len(u) - 1)
        points = int(points) # trunc
        l_total_points.append(points)
    # print(l_total_points)
    print(sum(l_total_points))


def load_card_info(test=True) -> list:
    ''' Return list of sets of numbers on each card'''
    # assumes that the scratch numbers cannot repeat
    if test:
        filepath = './test_input.txt'
    else:
        filepath = './input.txt'

    ret = []
    with open(filepath, 'r') as f:
        contents = f.read().split('\n')[:-1]
        for card in contents:
            winning_numbers = set()
            numbers = set()
            i = 0
            while card[i] != ':':
                i += 1
            buf = ''
            while card[i] != '|':
                buf += card[i]
                i += 1
            buf = buf[1:-1]
            for idx in range(int(len(buf) / 3)):
                j = idx * 3
                k = j + 3
                s = buf[j:k]
                num = int(s)
                winning_numbers.add(num)
            buf = ''
            while i < len(card):
                buf += card[i]
                i += 1

            buf = buf[1:]
            for idx in range(int(len(buf) / 3)):
                j = idx * 3
                k = j + 3
                s = buf[j:k]
                num = int(s)
                numbers.add(num)
            
            ret.append([winning_numbers, numbers])
    return ret








main()
