def check_fermat(a,b,c,n):
    temp=c**n
    sum=(a**n)+(b**n)
    if sum==temp:
        print("Holy smokes,Fermat was wrong!")
    else:
        print("No,that doesn't work")

def intake():
    a=int(input("Enter first value:"))
    b=int(input("Enter second value:"))
    c=int(input("Enter third value:"))
    n=int(input("Enter fourth value:"))
    check_fermat(a,b,c,n)

intake()