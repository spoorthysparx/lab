def gcd(n,m):
    smallest=min(n,m)
    if n==0 or m==0:
        return max(n,m)
    for i in range(1,smallest+1):
        if n%i==0 and m%i==0:
            gcd=i
    return gcd



n,m=int(input("Enter first number:")),int(input("Enter second number:"))           
print(gcd(n,m))