number=int(input("Enter a number:"))
sum=0
def sum_of_digit(number):
    global sum
    while(number!=0):
        reminder=number%10
        number=number//10
        sum=sum+reminder
    print(sum)

sum_of_digit(number)