# NEGATIVE INDEX IS ONESIDE
list1=[-3,-34,23,-12,55,-45,2,8,4]
index=0
m=[ ]
n=[ ]
o=[ ]
while index<len(list1):
	if list1[index]<0:
		m.append(list1[index])
	if list1[index]>=0 and list1[index]<=10:
		n.append(list1[index])
	if  list1[index]>=10:
		o.append(list1[index])
	index=index+1
print (m,n,o)
list1=m+n+o
print (list1)
j=0
sum1=0
while j<len(list1):
	sum1=sum1+list1[j]
	j=j+1
print (sum1)

