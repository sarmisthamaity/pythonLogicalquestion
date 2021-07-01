a=[45,67,89,23,12,11,7,99,21]
i=0
while i<len(a):
	j=0
	while j<len(a)-1:
		if a[j+1]<a[j]:
			a[j+1],a[j]=a[j],a[j+1]
		j=j+1
	i=i+1
print (a)

