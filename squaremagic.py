magic_square=[ 
	[8,3,4],
	[1,5,9],
	[6,7,2]
]
i=0
sumd1=0
sumd2=0
while i<len(magic_square):
	j=0
	sumr=0
	sumc=0
	while j<len(magic_square[i]):
		sumr=sumr+magic_square[i][j]
		sumc=sumc+magic_square[j][i]
		if i==j:
			sumd1=sumd1+magic_square[i][j]
		if i+j==len(magic_square)-1:
			sumd2=sumd2+magic_square[i][j]
		j=j+1
	i=i+1
	print (sumr,sumc)
print (sumd1,sumd2)
if sumr==sumc:
	print ("sumr")
if sumr==sumd1:
	print ("its magic_square")
else:
	print ("not magic_square")
	