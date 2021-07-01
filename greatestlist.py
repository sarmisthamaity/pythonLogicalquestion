# WHOSE LENGTH IS LONG
a=["poojadakjgjbavjhaedfyugahjf","komalhgfh","shubhangi"]
index=0
count_p=0
count_k=0
count=0
while index<len(a):
	index1=0
	while index1<len(a[index]):
		if (a[index])=="poojadakjgjbavjhaedfyugahjf":
			count_p=count_p+1
		if (a[index])=="komalhgfh":
			count_k=count_k+1
		if (a[index])=="shubhangi":
			count=count+1
		index1=index1+1
	index=index+1
print (count_p,count_k,count)
if count_p>count_k and count_p>count:
	print ("count_p is greater")
if count_k>count and count_k>count_p:
	print ("count_k is greater")
if count>count_k and count>count_p: 
	print ("count is greater")


# 2ND TYPE
i=["sarmistha","gouri123456","swapansaroj"]
index=0
b=0
a=0
n=0
m=[ ]
while index<len(i):
    j=0
    count=0
    while j<len(i[index]):
        count=count+1
        if b<=count:
            b=count
            a=i[index]
        m.append(a)
        print (m)
        j=j+1
    index=index+1
print ("this is longest length",b,"this is element",a)




