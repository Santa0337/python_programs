n=int(input("Enter the value of n:"))
sum=0
temp=n
while temp>0:
    r=temp%10
    sum=sum*10+r
    temp=temp//10
if n==sum:
    print("Palindrome number")
else:
    print("Not a palindrome number")