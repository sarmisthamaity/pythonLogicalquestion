n=[10,11,12,13,14,17,18,19]
i=0
c=[ ]
while i<len(n):
	j=i
	d=[ ]
	while j<len(n):
		if n[i]+n[j]==30:
			d.append(n[i])
			d.append(n[j])
			c.append(d)
			break
		j=j+1
	i=i+1
print (c)

