r = {}
n = int(input("Enter no.of entries:"))
for _ in range(n):
    device,vlan=str(input("Enter device and vlan:")).split()
    if device not in r:
        r[device] = []
    r[device].append(vlan)
print(r)