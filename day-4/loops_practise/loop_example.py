password = "Panda008"
a = 0
while a<3:
    pas = input("Enter password: ")
    if(pas==password):
        print("You Entered Right Password:", pas)
        print("You are Entre your Device")
        break
    else:
        print("You Entered Wrong Password:")
        if(a==2):
            print("You are 3 Time Entred Wrong Password")
        a+=1
    # pas = input(" Please Enter Correct Password: ")
    if a >= 3:
        print("Your password entry limit for today is over")
        break
        
    



