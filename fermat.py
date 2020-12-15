"""Fermat’s Last Theorem says that there are no positive integers a, b, and c such that a​n​ + b​n​ = c​n​ for any values of n greater than 21.
Write a function named check_fermat that takes four parameters a, b, c and n- and checks to see if Fermat’s theorem holds.
If n is greater than 2 and  a​n​ +b​n​ = c​n​ the program should print, “Holy smokes, Fermat was wrong!”
Otherwise the program should print, “No, that doesn’t work.”2.
Write a function that prompts the user to input values for a, b, c and n,converts them to integers, and uses check_fermat to check whether theyviolate Fermat’s theorem."""

def check_fermat(a,b,c,n):
    temp=c**n
    sum=(a**n)+(b**n)
    if sum==temp:
        print("Holy smokes,Fermat was wrong!")
    else:
        print("No,that doesn't work")

def main():
    a=int(input("Enter first value:"))
    b=int(input("Enter second value:"))
    c=int(input("Enter third value:"))
    n=int(input("Enter fourth value:"))
    check_fermat(a,b,c,n)

main()