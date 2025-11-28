# user to enter password is correct  or not 

password="Panda008"

pas=input("Entre password :")
while(pas != password):
    print(" You Entred Wrong password: ",pas)
    print("please Entre Correct password")
    
    pas=input("Entre password :")

print("You Entred Right password")
