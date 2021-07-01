string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
index=0
m=[ ]
while index<len(string_list):
	j=0
	while j<len(string_list[index]):
		if string_list[index] not in m:
			m.append(string_list[index]) 
		j=j+1
	index=index+1
print(m)
