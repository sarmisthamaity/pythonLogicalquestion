paisa=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
counter=0
crore=0
lakh=0
dilwale=0
while counter<len(paisa):
	if paisa[counter]>=10000000:
		crore=crore+1
	elif paisa[counter]>=100000:
		lakh=lakh+1
	elif dilwale<=100000:
		dilwale=dilwale+1
	counter=counter+1
print ("crorepati",crore)
print ("lakhpati",lakh)
print ("dilwale",dilwale)