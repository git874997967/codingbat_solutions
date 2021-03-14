def rotate(str):
    i = 0
    str = list(str)
    while i < len(str) - 1:
        str[i],str[i+1] = str[i+1] ,str[i]
        i += 2
    print(''.join(str))
def removeIndex(str,index):
    result = ''
    for i in range(len(str)):
        if i % index == 0:
            continue
        else:
            result += str[i]
    print(result) 
#print(rotate("abc3qd1234567891"))
removeIndex("abc3qd1234567891",3)



