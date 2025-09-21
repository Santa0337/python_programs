import re
# arp-a

# inp="""
#   Internet Address      Physical Address      Type
#   10.1.1.1              0030.f29b.0c01        dynamic
#   10.1.1.2              000d.bd5d.2eb0        dynamic
# """
# out = re.findall(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F\.]+)\s+(\w+)', inp)
# for ip,mac,dyn in out:
#     print(f"IP: {ip}, MAC: {mac}, Type: {dyn}")


#show mac address-table dynamic
# import re
# mac="""
#           Mac Address Table
# -------------------------------------------

# Vlan    Mac Address       Type        Ports
# ----    -----------       --------    -----

#    1    0001.9722.000d    DYNAMIC      Fa0/2
#    1    000d.bd5d.2eb0    DYNAMIC      Fa0/1
#    1    0030.f29b.0c01    DYNAMIC      Fa0/3
# """
# out= re.findall(r"(\d+)\s+([0-9a-zA-Z\.]+)\s+(\S+)\s+(\S+)",mac,re.MULTILINE)
# for vlan,mac,Type,ports in out:
#     print(f"Vlan: {vlan}, MAC: {mac}, Type: {Type}, Ports: {ports}")

#ipconfig

# inp ="""
# FastEthernet0 Connection:(default port)

#    Connection-specific DNS Suffix..: 
#    Link-local IPv6 Address.........: FE80::201:97FF:FE22:D
#    IPv6 Address....................: ::
#    IPv4 Address....................: 10.1.1.3
#    Subnet Mask.....................: 255.0.0.0
#    Default Gateway.................: ::
#                                      10.1.1.1

# Bluetooth Connection:

#    Connection-specific DNS Suffix..: 
#    Link-local IPv6 Address.........: ::
#    IPv6 Address....................: ::
#    IPv4 Address....................: 0.0.0.0
#    Subnet Mask.....................: 0.0.0.0
#    Default Gateway.................: ::
#                                      0.0.0.0
# """
# pattern = re.compile(
#     r"IPv4 Address.*?:\s*((?:\d{1,3}\.){3}\d{1,3}).*?"
#     r"Subnet Mask.*?:\s*((?:\d{1,3}\.){3}\d{1,3}).*?"
#     r"Default Gateway.*?:\s*(?:(?:::+)?\s*)?((?:\d{1,3}\.){3}\d{1,3})",
#     re.MULTILINE | re.DOTALL
# )

# out = re.findall(pattern,inp)
# for ip,mask,gateway in out:
#     print(f"IP: {ip}, Mask: {mask}, Gateway: {gateway}")
#     break


#show ip int brief

# inp="""
# Interface              IP-Address      OK? Method Status                Protocol 
# GigabitEthernet0/0/0   10.1.1.1        YES manual up                    up 
# GigabitEthernet0/0/1   11.1.1.1        YES manual up                    up 
# GigabitEthernet0/0/2   unassigned      YES unset  administratively down down 
# Vlan1                  unassigned      YES unset  administratively down down
# """

# out = re.findall(r'(\S+)\s+((?:\d{1,3}\.){3}\d+|\S+)\s+\S+\s+\S+\s+(administratively down|up)\s+(down|up)', inp, re.MULTILINE)
# print(out)



#show ip route

# inp="""
# Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
#        D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
#        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
#        E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
#        i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
#        * - candidate default, U - per-user static route, o - ODR
#        P - periodic downloaded static route

# Gateway of last resort is not set

#      10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
# C       10.0.0.0/8 is directly connected, GigabitEthernet0/0/0
# L       10.1.1.1/32 is directly connected, GigabitEthernet0/0/0
#      11.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
# C       11.0.0.0/8 is directly connected, GigabitEthernet0/0/1
# L       11.1.1.1/32 is directly connected, GigabitEthernet0/0/1
# """
# out = re.findall(
#     r"C\s+((?:\d{1,3}\.){3}\d{1,3}/\d+).*?(\S+)$",inp,
#     re.MULTILINE
# )
# print(out)

#show ip route rip

# inp="""
#      3.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
# R    4.0.0.0/8 [120/1] via 2.0.0.2, 00:00:08, Serial0/1/0
# R    5.0.0.0/8 [120/1] via 3.0.0.2, 00:00:17, GigabitEthernet0/1
# R    6.0.0.0/8 [120/2] via 2.0.0.2, 00:00:08, Serial0/1/0
# R    7.0.0.0/8 [120/2] via 3.0.0.2, 00:00:17, GigabitEthernet0/1
# R    8.0.0.0/8 [120/3] via 3.0.0.2, 00:00:10, GigabitEthernet0/1
#                [120/3] via 2.0.0.2, 00:00:08, Serial0/1/0
# R    9.0.0.0/8 [120/3] via 3.0.0.2, 00:00:17, GigabitEthernet0/1
# """
# out=re.findall(r'(?:R\s+)?((?:\d{1,3}\.){3}\d+/\d+).*?via\s+((?:\d{1,3}\.){3}\d+),.*?,\s*(\S+)',inp,re.MULTILINE)
# print(out)

#show arp

# inp="""
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  1.0.0.1                 -   000C.8544.5101  ARPA   GigabitEthernet0/0
# Internet  3.0.0.1                 -   000C.8544.5102  ARPA   GigabitEthernet0/1
# Internet  3.0.0.2                 25  0060.5C01.7201  ARPA   GigabitEthernet0/1
# """
# out=re.findall(r'\S+\s+((?:\d{1,3}\.){3}\d+)\s+\S+\s+([0-9a-zA-Z\.]+)\s+\S+\s+(\S+)',inp,re.MULTILINE)
# print(out)


