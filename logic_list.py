# nested list convert into a list
list1=[[23,45,12],[11,56,78],[89,90,66]]
i=0
m=[ ]
while i<len(list1):
	j=0
	while j<len(list1[i]):
		m.append(list1[i][j])
		j=j+1
	i=i+1
print (m)


# SORT WITHOUT CHANGE -1 INDEX
list1=[-1,5,190,170,-1,-1,160,67]
i=0
while i<len(list1):
	j=i+1
	while j<len(list1)-1:
		if list1[i]<0: 
			j=j+1
		else:
			list1[j]>list1[i]
			b=list1[i]
			list1[j]=list1[i]
			list1[j]=b
		j=j+1
	i=i+1
print (list1)




