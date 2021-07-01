# 1 se 1000 tak saare numbers print karne ka loop likho. Lekin

# Agar number 3 se divisible hai toh "nav" print karvao.
# Agar number 7 se divisible hai toh "gurukul" print karvao.
# Agar number 21 se divisible hai toh "navgurukul" print karvao.


index=0
while index<1000:
	if index%3==0:
		print (index,"nav")
	if index%7==0:
		print (index,"gurukul")
	if index%21==0:
		print (index,"navgurukul")
	index=index+1
