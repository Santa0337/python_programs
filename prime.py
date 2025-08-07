n=int(input("Enter the value of n:"))
count=0
for i in range(2,n+1):
    if n%i==0:
        count+=1
if count==1:
    print("Prime number")
else:
    print("Not a prime number")