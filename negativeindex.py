list1=[-1,143,87,67,-1,-1,213,567]
index=0
m=0
while index<len(list1):
    i=index
    while i<len(list1):
        if list1[index]<=list1[i] or list1[index]!=-1 and list1[i]==-1:
            m=list1[index]
            i=i+1
        else:
            list1[index]=list1[i]
            list1[i]=m
    index=index+1
print (list1)



list1=[-1,143,87,67,-1,-1,213,567]
index=0
while index<len(list1):
	j=1
	while j<len(list1)-1:
		if list1[index]<=-1:
			break
		j=j+1
	else:
		if list1[j-1]>=0:
			if list1[j]<list1[j-1]:
				b=list1[j]
				list1[j]=list1[j-1]
				# list1[j-1]=b
			j=j+1
	index=index+1
print (list1)
