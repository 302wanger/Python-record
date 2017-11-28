#
f = open("self_use.txt",'r').readlines()
for line in f:
    line = line.strip()
a = []
for i in f:
    a.append(i)
a = [i.replace("\n","") for i in a]

#
f = open("self_use_b.txt",'r').readlines()
for line in f:
    line = line.strip()
b = []
for i in f:
    b.append(i)

b = [i.replace("\n","") for i in b]

#
c= []
for x in b:
    for x  not in a:
        c.append(x)
c = [i.replace("\n","") for i in c]


c.append(list(set(b).difference(set(a)))) # b have and a don't have


# print c in a readable way
for i in range(len(c[0])):
    print(c[o][i])
