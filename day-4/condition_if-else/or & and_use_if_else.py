# or use in if-else statment 
# # Animal name find in message               
c1="dog"
c2="cat"
c3="monkey"
c5="donkey"
c4="lion"

# Entre animal name
dot=input("Entre four  animal name :")

#if name in
if((dot in c1) or (dot in c2) or (c3 in dot) or (c4 in dot)):
    print("you are lose the Game")
else:
    print("you are win game")


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



