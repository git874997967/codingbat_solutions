def string_bits(str):
    print(str[::-1])
    for i in range(len(str)):
        print(str[i])
    return str[::2]
print(string_bits("abcdefg"))