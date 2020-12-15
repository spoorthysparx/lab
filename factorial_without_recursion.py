""" write a prgram to find out the factorial of a number using loops"""

n=int(input("Enter the number:"))
def fact_without_recursion(n):
    fact=1
    if n<0:
        print("Factorial doesn't exist ")
    else:
        for i in range (1,n+1):
            fact*=i
        print("Factorial of",n,"is",fact)

fact_without_recursion(n)