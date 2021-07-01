elements=[23,14,56,12,19,9,15,25,31,42,43]
counter=0
even=0
odd=0
while counter<len(elements):
	if elements[counter]%2==0:
		even=even+1
	else:
		odd=odd+1
	counter=counter+1
print ("even",even)
print ("odd",odd)

