digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

# Current bug: strings like "twone" have 1 as last digit
def find_patterns_in_substring(string:str) -> list:
    # look for first number in string
    # add string to ret
    # delete first [len] char from string
    # restart

    ret = []
    while True:
        idxs = []
        for pattern in digits:
            idx = string.find(pattern)
            if idx >= 0:
                idxs.append([idx, pattern])
        if len(idxs) != 0:
            first_num_in_string = sorted(idxs, key=lambda x: x[0])[0]
            ret.append(first_num_in_string[1])
            string = string[first_num_in_string[0] + 1:]
        else:
            break
    return [digits[p] for p in ret]
        

def test():
    with open('./input.txt', 'r') as f:
        contents = f.readlines()
    line = contents[2]
    print(line)
    print(find_patterns_in_substring(line))
    

def main():
    with open('./input.txt', 'r') as f:
        contents = f.readlines()
    nums = []
    for line in contents:
        sub_string = ''
        first = None
        last = None

        for char in line:
            if char.isnumeric():
                p = find_patterns_in_substring(sub_string)
                if len(p) != 0 and first is None:
                    first = p[0]
                if first is None:
                    first = int(char)
                else:
                    last = int(char)
                sub_string = ''

            elif char.isalpha():
                if sub_string == '':
                    sub_string = char
                else:
                    sub_string += char

         
        p = find_patterns_in_substring(sub_string)
        if len(p) != 0:
            if first is None:
                first = p[0]
            last = p[-1]

        if last is None:
            last = first
        num = first * 10 + last
        nums.append(num) 

    print(sum(nums))

# test()
main()
