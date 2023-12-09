import re
from tqdm import tqdm

def main():
    data = load_file(test=False)
    seeds, maps = parse_data(data) 
    print('parsed_data')
    max_location = 0
    for seed_gen in tqdm(seeds):
        for seed in tqdm(seed_gen):
            path = trace_path(seed, maps)
            # print(seed, 'location @', path[-1])
            if max_location < path[-1]:
                max_location = path[-1]
    print(min(locations))

def trace_path(seed:int, maps:dict) -> list:
    ret = []
    current_source = 'seed'
    num = seed
    flag = True
    while flag:
        flag = False
        for source, dest in maps:
            if source == current_source:
                # print(source, dest)
                flag = True
                flag2 = False
                for l in maps[source,dest]:
                    if (l[1] <= num) and (num < l[1] + l[2]) and not flag2:
                        # print('bounds', l[1], l[1] + l[2])
                        # print(f"{source} number {num} -> {dest} number ", end='')
                        num = l[0] + num - l[1]
                        ret.append(num)
                        # print(num)
                        current_source = dest
                        # print('set new source to', current_source)
                        flag2 = True
                if not flag2:
                    # print(f'failed to find mapping for {source} to {dest}')
                    current_source = dest
                    ret.append(num)
    return ret 


def parse_data(data):
    seeds = [int(i) for i in re.split(":? ", data[0])[1:]]
    seeds2 = []
    assert len(seeds) % 2 == 0
    for i in range(int(len(seeds) / 2)):
        j = i * 2
        seeds2.append(range(seeds[j], seeds[j] + seeds[j+1]))
    maps = {}
    for i, line in enumerate(data):
        if re.match('.+-', line):
            source, destination = re.split('-to-', line[:-5])
            maps[(source, destination)] = []
        elif re.match('\d+ \d+ \d+', line):
            maps[(source, destination)].append(list(map(int, line.split(' '))))
    return seeds2, maps


def load_file(test=True):
    if test and 1:
        filename = './test_input.txt'
    else:
        filename = './input.txt'
    with open(filename, 'r') as f:
        contents = re.split('\n+', f.read())[:-1]

    return contents

main()
