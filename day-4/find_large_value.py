
user1=int(input("Entre a number:"))
user2=int(input("Entre a number:"))
user3=int(input("Entre a number:"))

# if(user1>user2):
#     print("")
#     if(user1>user3):
#        print("number 1 is big",user1)
#     else:                               # same as lower codee
#        print("number 3 is big",user3)
# elif(user2>user3):
#     print("number 2 is big",user2)
# else:
#     print("number 3 is big",user3)

if(user1>user2 and user1>user3):
    print("number 1 is bigg",user1)
elif(user2>user3):
    print("number 2 is bigg",user2)
else:
    print("number 3 is big",user3)
