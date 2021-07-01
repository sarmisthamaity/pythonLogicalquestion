elements=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even=0
odd=0
even_sum=0
odd_sum=0
i=0
while i<len(elements):
	if elements[i]%2==0:
		even=even+1
		even_sum=even_sum+elements[i]
	else:
		odd=odd+1
		odd_sum=odd_sum+elements[i]
	i=i+1
even_average=even_sum/even
odd_average=odd_sum/odd
print ("even",even_average)
print ("odd",odd_average)