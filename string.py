mainstr="the quick brown fox jumped over the lazy dog,the dog slept over the verandha"
substr="over"
str1="on"
string2=mainstr.split()
i=0
j=" "
while i<len(string2): 
	if string2[i] == substr:
		j=j+str1+" "
	else:
		j=j+string2[i]+" "
	i=i+1
print (j)

