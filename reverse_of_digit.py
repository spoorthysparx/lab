"""write a program to find out the reverse of the digit"""

number=int(input("enter a number:"))
reverse=0
def reverse_of_digit(number):
    global reverse
    while(number>0):
        reminder=number%10
        reverse=(reverse*10)+reminder
        number=number//10
    print(reverse)

reverse_of_digit(number)