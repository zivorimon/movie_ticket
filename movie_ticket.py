#date 24/4/2025

age=int(input("what is your age?:")) 
day=input("when you want the tickect weekday/weekend?:").lower()     
mem=input("are you a member? y/n :").lower()
ticket_price=0
child=age<13
elder=age>=6
B_price= 20

sen1 = day == "weekday" and mem == "y"
sen2 = day == "weekday" and mem == "n"
sen3 = day == "weekend" and mem == "y"
sen4 = day == "weekend" and mem == "n"

if day not in ["weekday" , "weekend"]:  
	print("invalid day")
	exit()

if mem not in ["y" , "n"]:
        print("error member")
        exit()




if age<13 and age>0:

	if sen1:
		print(f"your ticket price is {B_price*0.5-2}")
	
	elif sen2:
		print(f"your ticket price is {B_price*0.5}")

	elif sen3:
		print(f"your ticket price is {B_price*0.5+3}")

	elif sen4:
		print(f"your ticket price is {B_price*0.5+5}")

elif age>=60:

	if sen1:
		print(f"your ticket price is {B_price*0.3-2}")

	elif sen2:
		print(f"your ticket price is {B_price*0.3}")

	elif sen3:
		print(f"your ticket price is {B_price*0.3+3}")

	elif sen4:
		print(f"your ticket price is {B_price*0.3+5}")


elif age>=13 and age <60:

	if sen1:
		print(f"your ticket price is {B_price-2}")

	elif sen2:
		print(f"your ticket price is {B_price}")

	elif sen3:
		print(f"your ticket price is {B_price+3}")

	elif sen4:
		print(f"your ticket price is {B_price+5}")

elif age == 0:
	print("invalid age")




