low=int(input("Enter the low value"))
high=int(input("Enter the high value"))
for num in range(low,high):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)