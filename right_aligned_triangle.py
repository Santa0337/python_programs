a = int(input("Enter a number: "))

for i in range(a + 1):
    print(' ' * (a - i) + '*' * i)
