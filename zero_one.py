# PATTERN 	1
		#   01
		#   101
		#   0101
		  # 10101


i=1
while i<=5:
    j=0
    while j<i:
        if (i+j)%2==1:
            print("1",end="")
        else:
            print("0",end="")
        j=j+1
    print()
    i=i+1

    