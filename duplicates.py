n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13,11]
i=0
s=[ ]
while i<len(n):
	count=0
	j=0
	while j<len(n):
		if n[i]==n[j]:
			count=count+1
			if count==2 and n[i] not in s:
				s.append(n[i])
		j=j+1
	i=i+1
print (s)


list1=[23,67,89,34,16,7]
list2=[34,12,16,89,45,23]
index=0
m=[ ]
while index<len(list1):
	j=0
	while j<len(list2):
		if list1[index]==list2[j]:
			m.append(list1[index])
		j=j+1
	index=index+1
print (m)
a=0
n=[ ]
while a<len(m):
	b=m[a]*m[a]
	n.append(b)
	a=a+1
print (n)







