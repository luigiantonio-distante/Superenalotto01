"""
x="78 21 18 25 30 76"
l=x.split(" ")
i=0
while i<len(l):
    l[i]=int(l[i])
    i+=1
print(l)
"""

L = ["10", "20", "90", "80", "60", "70"]
M = [int(x) for x in L]
print(M)

