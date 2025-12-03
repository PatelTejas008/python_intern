# user to enter password is correct  or not 

# password="Panda008"

# a=0
# pas=input("Entre password :")
# while(pas != password):
#     print(" You Entred Wrong password: ",pas)
#     a+=1
#     if(a>=3):
#         print("Your today Password Entre limit is over  ")
#         exit()

    
#     pas=input("Entre password Corret Password:")


# print("You Entred Right password")

password = "Panda008"

a = 0

pas = input("Enter password: ")
while pas != password:
    print("You Entered Wrong Password:", pas)
    a += 1

    pas = input("Enter Correct Password: ")
    if a >= 3:
        print("Your password entry limit for today is over!")
        break
        exit()
    



