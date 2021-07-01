
# DIFFERENCE IN TWO LIST
list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
# c is empty list
c=[ ]
index=0
while index<len(list2):
	if list1[index] not in list2:
		c.append(list1[index])
	index=index+1
print (c)