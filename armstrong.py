n=int(input("Enter the value of n:"))
num_of_digits=len(str(n))
sum=0
temp=n
while temp>0:
    r=temp%10
    sum=sum+r**num_of_digits
    temp=temp//10
if sum==n:
    print("Armstrong number")
else:
    print("Not an armstrong number")