"""write a program to find out the square root of the given number using Newton's method"""

def get_square_root(number,precision):
    sqroot = number
    while abs(number - sqroot*sqroot)>precision:
        sqroot=(sqroot+number/sqroot)/2
    return sqroot

number=int(input("Enter the digit:"))
precision= 0.001
print(get_square_root(number,precision))
