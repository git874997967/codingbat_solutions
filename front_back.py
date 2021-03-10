def front_back(str):
    print(str[::])
    print(str[1:-1])
    return str if len(str) <= 1 else str[-1] + str[1: len(str) - 1] + str[0]

str = 'abcdefg'
front_back(str)
