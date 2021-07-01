a=['n','i','t','i','n']
# b empty list
b=[]
# i for index
i=len(a)-1
while i>=0:
	b.append(a[i])
	i=i-1
print (b)
if a==b:
	print ("palindrome")
else:
	print ("not palindrome")
