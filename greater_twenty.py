n=[23,45,67,89,12,11,10,21,32,13,16]
index=0
length=len(n)
greater_20=0
less_40=0
while index<length:
	b=n[index]
	if b<40:
		less_40=less_40+1
	if b>20:
		greater_20=greater_20+1
	index=index+1
print ("less_40:",str(less_40))
print ("greater_20:",str(greater_20))