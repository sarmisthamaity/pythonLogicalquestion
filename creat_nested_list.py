lis=[]
i=1
while i<=17:
    lis.append(i)
    i=i+1
j=0
b=1
d=[]
a=[]
f=[]
m=[]
w=[]
while j<len(lis):
    if lis[j]<=5:
        d.append(lis[j])
    elif lis[j]<=10:
        m.append(lis[j])
    elif lis[j]<=15:
        a.append(lis[j])
    else:
        f.append(lis[j])
    j=j+1
w.append(d)
w.append(m)
w.append(a)
w.append(f)
print(w)
