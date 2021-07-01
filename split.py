def break_into_words(sentence):
	new_list=[ ]
	# new_list is for 
	i=0
	# i is for index
	while i<len(sentence):
		j=i
		# j is index for inner while loop
		m=" "
		while j<len(sentence):
			if sentence[j]!=" ":
				m=m+sentence[j]
			else:
				break
			j=j+1
		new_list.append(m)
		i=j+1
	return new_list
line="NavGurukul is an alternative to higher education reducing the barriers of current formal education system"

print (break_into_words(line))

