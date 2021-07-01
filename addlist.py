list1=[1,2,3],[3,4,5],[34,54,56],[12,31,23]
index=0
while index<len(list1):
	i=0
	sum1=0
	while i<len(list1[index]):
		sum1=sum1+list1[index][i]
		i=i+1
	index=index+1
	print (sum1)
