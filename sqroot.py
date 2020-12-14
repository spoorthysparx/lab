def get_square_root(number,precision):
    sqroot = number
    while abs(number - sqroot*sqroot)>precision:
        sqroot=(sqroot+number/sqroot)/2
    return sqroot

number=7
precision= 0.001
print(get_square_root(number,precision))
