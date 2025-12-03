while True:
    Balance=5000

    print("Check Balance Press 1:")
    print("Money Deposit Press 2:")
    print("Money withdraw Press 3:")
    print("Exit Press 4:")

    choice=int(input("Option select for Banking service :"))

    if(choice==1):
        print(f"Your Balance is :{Balance}")
    elif(choice==2):
        depo=int(input("Entre the Amount you add in bank: "))
        Balance += depo
    # print(f"Your balance:{Balance}")
        print(f"Your Balance is :{Balance}")

    elif(choice==3):
        amount=int(input("Entre the Amount you wany to withdraw :"))
        if amount<=Balance:
            Balance-=amount
            print(f" Your latest Balance is :{Balance}")
        else:
            print("You have not Insufficient balance")

    if(choice==4):
        print(f"Thank you")
        break

    again=input("Entre yes/no for continue atm service use")
    if(again=="no"):
        print("Thanks you ")
    elif(again=="yes"):
         continue
    else:
        print("please entre yes/no")
