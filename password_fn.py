def password_function(password):
	if len(password)>=6 or len(password)<=16:
		if password>"0" or password<"9":
			if "$" in password:
				if password>"A" or password<"z":
					return (password,"is strong password")

	else:
		return (password,"password is weak")

pas=input("enter ur password: ")

print (password_function(pas))

