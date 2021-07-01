list1=[23,45,12,11,89,6]
index=0
maxi=0
while index<len(list1):
	if maxi<list1[index]:
		maxi=list1[index]
	index=index+1	
big=maxi
secmax=0
i= 0
while i<len(list1):
	if maxi >list1[i] and secmax<list1[i]:
		secmax=list1[i]
	i=i+1
print ("secmax",secmax)
print("max=",big)
