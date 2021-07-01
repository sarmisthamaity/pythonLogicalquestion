marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
index=0
while index<len(marks):
	j=0
	max1=0
	while j<len(marks[index]):
		if max1<marks[index][j]:
			max1=marks[index][j]
		j=j+1
	index=index+1
	print (max1)


