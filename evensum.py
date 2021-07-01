elements=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even_sum=0
odd_sum=0
counter=0
while counter<len(elements):
	if elements[counter]%2==0:
		even_sum=even_sum+elements[counter]
	else:
		odd_sum=odd_sum+elements[counter]
	counter=counter+1
print ("even_sum",even_sum)
print ("odd_sum",odd_sum)