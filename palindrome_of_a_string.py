s ="abc"
b = ""
for i in range(len(s)-1,-1,-1):
    b = b+s[i]
if b == s:
    print("palindrome")
else:
    print("not a palindrome")