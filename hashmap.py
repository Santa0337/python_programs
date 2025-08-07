list=[1,1,1,1,2,2,3,4]
d={}
for i in list:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)