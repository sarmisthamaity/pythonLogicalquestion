list1=[1,2,3,4,5,6,7,8,9]
index=0
list2=[ ]
c=[ ]
while index<len(list1):
    if list1[index]%2==0:
        list2.append(list1[index])
    else:
        c.append(list1[index])
    index=index+1
print(list2)
m=[ ]
i=len(list2)-1
while i>=0:
    print (list2[i])
    m.append(list2[i])
    i=i-1
print (m)
lis=m+c
print (lis)
