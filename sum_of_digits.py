number=int(input("Enter a number:"))
sum=0
while(number!=0):
    reminder=n%10
    number=number//10
    sum=sum+reminder
print(sum)