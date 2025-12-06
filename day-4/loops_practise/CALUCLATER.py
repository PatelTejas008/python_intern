while True:

    print("This caluclate 2 numbers")
    print("Press 1 for addition +++")
    print("Press 2 for minus ---")
    print("Press 3 for multiple ***")
    print("Press 4 for divied ///")
    print("Press 5 for exit")


#choice Entre what do you want +,-,*,%
    choice =int(input("Entre 1 to 4 number :"))

    if(choice==5):
     print("Exit the calculater")
     break

    num1=float(input("Entre the first number :"))
    num2=float(input("Entre the second number :"))


    if choice==1:
        print(f"{num1} + {num2} = ",num1+num2)
    elif choice==2:
        print(f"{num1} - {num2} = ",num1-num2)
    elif choice==3: 
     print(f"{num1} X {num2} = ",num1*num2)
    elif choice==4: 
        if(num2 and num1==0):
            if(num1 == 0):
                print(f"Entre {num1} number is 0\n 0 can't divide any value")
            elif(num2 == 0):
                print(f"Entre {num2} number is 0\n 0 can't divide any value")
         
        else:
            print(f"{num1} % {num2} = ",num1/num2)
    else:
     print(" invalid choice \n Entre the number in 1 to 4 ")

# print("Entre yes to calulate another value \nEntre no for 'EXIT'")
    again=input("Entre yes/no :")
    if(again=="yes"):
        print("yes continue the caluclater")
    elif(again=="no"):
        print("Thnaks You")
        break
    
