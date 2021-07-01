n=int(input("enter number: "))
s=0
num=n
while n>0:
    rem=n%10
    print(rem)
    i=1
    fact=1
    while i<=rem:
        fact=fact*i
        i=i+1
    print(fact)
    s=s+fact
    print(s)
    n=n//10
print(s)
if s==num:
    print("strng")
else:
    print("not strong")
	

