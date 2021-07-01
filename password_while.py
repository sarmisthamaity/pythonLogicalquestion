password=input("enter tha password:")
i=0
while i<len(password):
    if i==8:
        if password>="A" or password<="z":
            if password>="0" or password<="9":
                if "@" or "$" in password:
                    print ("password is valid")
    else:
        print ("not valid")
    i=i+1