print("Welcome to the tip calculator")
s=float(input("What is the total bill? "))
p=float(input("What percentage tip would you like to give? 10, 12, 15? "))
q=input("How many people to split the bill? ")
l=float((1+(p/100)))
z=(round((float(s)/float(q))*l,2))
t="{:.2f}".format(z)
print(f"Each person should pay {t}")