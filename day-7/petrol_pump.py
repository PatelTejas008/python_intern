print("\nchoose your fuel type")
print("1 For Petrol(94.69)")
print("2 For diesel(90.14)")
total_cost=0

while True:
    fuel=int(input("Entre 1 and 2 : "))
   
    if fuel==1:
        print("You choose petrol for your vehicle ")
        ad=input("Entre yes for confirm petrol\n else write no :").lower()
        if ad =="yes" or "y":
            print("ok")
        elif ad=="no":
            break
        liter=float(input("Entre how much fuel you want :"))

        total_cost=94.69*liter

    elif fuel==2:
        print("You choose diesel for your vehicle ")
        ad=input("Entre yes for confirm diesel\n else write no").lower()
        if ad =="yes" or "y":
            print("ok")
        elif ad=="no":
            break
        liter=float(input("Entre how much fuel you want :"))

        total_cost=90.14*liter

# if v in fuel==1:
#     print("petrol")
#     print("petrol price is 94.16")
#     print(f"petrol vehicle Entred {liter}")
print(f"For Fuel You pay Amount is {total_cost}")

# elif v in fuel==2:
#     print("diesel")
#     print("diesel price is 94.16")
#     print(f"diesel vehicle Entred {liter}")
#     print(f"For Fuel You pay Amount is {total_cost}")

