# NUMBER COUNT OCCURENCES
f=[4,7,2]
n=[2,5,4,2,5,9,3,7,3,4]
index1=0
s=[ ]
while index1<len(f):
	value=f[index1]
	count=0
	index2=0
	t=[ ]
	while index2<len(n):
		if value==n[index2]:
			count=count+1
		index2=index2+1
	t.append(value)
	index1=index1+1
	t.append(count)
	s.append(t)
print (s)
