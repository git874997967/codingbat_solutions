def string_match(a, b):
    # count = 0
    # if not a or not b or len(a) < 2 or len(b) < 2:
    #     return count

    # for i in range(len(a)-1):
    #     for j in range(len(b) - 1):
    #         if a[i:i + 2] == b[j:j + 2]:
    #             print(a[i:i + 2], b[j:j + 2],i,j)
    #             count += 1
    # return count
    if not a or not b or len(a) < 2 or len(b) < 2:
        return 0
    count = 0
    shorter = min(len(a),len(b))
    for i in  range(shorter - 1):
        if a[i:i + 2] == b[i:i + 2]:
            count += 1
    return count


print(string_match('aaxxaaxx', 'iaxxai'))  # 5

print(string_match('aabbccdd', 'abbbxxd')) # 5