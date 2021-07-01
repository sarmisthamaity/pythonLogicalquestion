list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
c=[]
index=0
while index<len(list2):
	if list1[index] not in list2:
		c.append(list1[index])
	index=index+1
print (c)

list1=[1,2,3,4,5,6]
list2=[2,3,1,0,7,6]
i=0
c=[]
d = []
while i<len(list1):
	j = 0
	while j<len(list2):
		if list1[j] not in list2:
			d.append(list1[j])
		j=j+1
	i=i+1
print (d)


















