from pprint import pprint

def main():
    data = load_card_info(test=False)
    # pprint(data)
    points = []
    number_of_matching_numbers = []
     
    for card in data:
        u = card[0].intersection(card[1])
        p = 2 ** (len(u) - 1)
        p = int(p) # trunc p < 1 to 0
        points.append(p)
        number_of_matching_numbers.append(len(u))
    
    number_of_copies = [0] * len(points)
    
    #Construct number_of_copies
    i = 0
    while i < len(points):
        for j in range(i+1, i+number_of_matching_numbers[i]+1):
            number_of_copies[j] += 1 + number_of_copies[i]
        i += 1

    for i in range(len(number_of_copies)):
        number_of_copies[i] += 1
    
    print(sum(number_of_copies))


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
