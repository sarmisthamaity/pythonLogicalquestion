# Q 2.Sort the letters in the string s by the order the occur in the string t.
# Example
# ● For s = "weather" and t = "therapyw", the output should be
# sortByString(s, t) = "theeraw";

s="weather"
t="threapyw"
st="theeraw"
index=0
b=" "
# b is empty string
while index<len(s):
    j=0
    # j is index for inner while loop
    while j<len(t):
        if st[index]==t[j] or st[index]==s[index]:
            b=b+t[j]
        j=j+1
    index=index+1
print (b)
