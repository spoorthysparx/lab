def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

a,b=int(input("Enter first number:")),int(input("Enter second number:"))
print(gcd(a,b))