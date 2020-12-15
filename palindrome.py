"""write a program to find out whether the given number is palindrome or not"""

number=int(input("Enter a number:"))
Temp=number
reverse=0
def palindrome(number):
    global reverse
    while(number>0):
        reminder=number%10
        reverse=(reverse*10)+reminder
        number=number//10
    if(Temp==reverse):
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")

palindrome(number)