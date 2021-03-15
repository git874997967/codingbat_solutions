def count_code(str):
    if not str or len(str) <= 3:
        return 0
    countCode = 0
    for i in range(0,len(str) - 3):
        subStr = str[i:i+4]
        print(subStr)
        if subStr[0] == 'c' and subStr[1] =='o' and subStr[-1] =='e':
            countCode += 1
    return countCode

print(count_code('codexxcode'))
