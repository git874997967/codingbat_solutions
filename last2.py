def last2(str):
    if len(str) < 2:
        return 0
    matchStr, count = str[-2:], 0
    for i in range(len(str) - 2):
        subStr = str[i:i+ 2]
        if subStr == matchStr:
            count += 1
    return count

