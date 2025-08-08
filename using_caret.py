string = "Python is high level language"
x = re.findall("^Python",string)
print(x)
if x:
  print("Found")
else:
  print("Not Found")
