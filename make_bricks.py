def make_bricks(small, big, goal):
    if (goal // 5 ) <= big and (goal % 5) <= small:
        return True
    elif 0 <= (goal - big * 5) <= small :
        return True
    return False

print(make_bricks(3,1,8))
print(make_bricks(7,1,11))
