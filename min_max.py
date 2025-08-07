list=[10,20,30]
smallest=list[0]
largest=list[0]
for num in list:
    if num<smallest:
        smallest=num

for num in list:
    if num>largest:
        largest=num
print(largest)
print(smallest)