# and operater use in if-else 

mark1=int(input("Entre the Maths marks:"))
mark2=int(input("Entre the science marks:"))
mark3=int(input("Entre the Hindi marks:"))

total=((mark1+mark2+mark3/300)*100)

if(total>=40 and marks>33 and mark2>33 and mark3>33):
    print("You are pass on exam",total)

else:
    print("Sorry but you are fail",total)
    print("pleas")



