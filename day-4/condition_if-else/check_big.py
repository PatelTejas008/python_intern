
user1=int(input("Entre a number:"))
user2=int(input("Entre a number:"))
user3=int(input("Entre a number:"))
user4=int(input("Entre a number:"))

if(user1>user2 and user1>user3 and user1>user4):
    print("Number 1 is bigg",user1)

elif(user2>user3 and user2>user4 ):
    print("Number 2 is bigg",user2)

elif(user3>user4 ):
    print("Number 3 is bigg",user3)

else:
    print("Number 4 is bigg",user4)