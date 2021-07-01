elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even=0
odd=0
even_sum=0
odd_sum=0
number=0
number_sum=0
i=0
while i<len(elements):
	number=number+1
	number_sum=number_sum+elements[i]
	if elements[i]%2==0:
		even=even+1
		even_sum=even_sum+elements[i]
	else:
		odd=odd+1
		odd_sum=odd_sum+elements[i]
	i=i+1
number_average=number_sum/number
even_average=even_sum/even
odd_average=odd_sum/odd
print ("number_average",number_average)
print ("even_average",even_average)
print ("odd_average",odd_average)