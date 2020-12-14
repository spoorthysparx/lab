def fact_with_recursion(n):
    if n==1:
        return 1
    else:
        return fact_with_recursion(n-1)*n

n=int(input("Enter the number:"))
print(fact_with_recursion(n))
