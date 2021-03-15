def cat_dog(str):
    if not str or len(str) < 3:
        return True 
    countCat = countDog = 0
    for i in range(0,len(str) - 2):
        print(str[i:i +3])
        if str[i:i +3] == 'cat':
            countCat += 1
        elif str[i :i + 3] == 'dog':
            countDog += 1
    print(countCat, countDog)
    return countCat == countDog

print(cat_dog('catcat'))
