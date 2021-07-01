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