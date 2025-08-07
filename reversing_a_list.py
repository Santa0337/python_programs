list=[1,2,3,4,5]
start=0
end=len(list)-1
while start<=end:
    list[start],list[end]=list[end],list[start]
    start=start+1
    end=end-1
print("Reversed list:",list)