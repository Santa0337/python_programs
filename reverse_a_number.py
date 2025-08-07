n=int(input("Enter the value of n:"))
reversed_num=0
temp=n
while temp>0:
    r=temp%10
    reversed_num=reversed_num*10+r
    temp=temp//10
print(reversed_num)