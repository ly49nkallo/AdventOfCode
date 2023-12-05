def main():
    with open('./input.txt', 'r') as f:
        contents = f.readlines()
    nums = []
    for line in contents:
        first = None
        last = None
        for char in line:
            if char.isnumeric():
                if first is None:
                    first = int(char)
                else:
                    last = int(char)
        if last is None:
            last = first
        num = first * 10 + last
        nums.append(num) 
    print(sum(nums))

main()
