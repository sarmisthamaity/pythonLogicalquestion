number=[50, 40, 23, 70, 56, 12, 5, 10, 7]
max=0
index=0
while index<len(number):
	if max<number[index]:
		max=number[index]
	index=index+1
b=max
secmax=0
s=0
while s<len(number):
	if b>number[s] and secmax<number[s]:
		secmax=number[s]
	s=s+1
print (secmax)
print ("max",b)