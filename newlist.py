list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
index=0
m=[ ]
while index<len(list1):
	j=0
	while j<len(list2):
		if list1[index]==list2[j]:
			if list1[index] not in m:
				m.append(list1[index])
		j=j+1
	index=index+1
print (m)


# 2ND TYPE
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
index=0
m=[ ]
while index<len(list1):
	j=0
	while j<len(list2):
		if list1[index]==list2[j] or list1[index]!=list2[j]:
			if list1[index]not in m and list2[j] not in m:
				m.append(list1[index])
		j=j+1
	index=index+1
print(m)
