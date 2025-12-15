while True:
    print("\nFule Types avilable are Petrol and diesel")
    print("1 for petrol")
    print("2 for diesel")
    fuel=int(input("Entre fule Type 1/2 :"))

    if fuel==1:
        Liter_price=94.14
        Fuel_type="Petrol"

    elif fuel==2:
        Liter_price=90.14
        Fuel_type="diesel"

    else:
        print("Invalid Entre 1 or 2")
        continue
         
    liter=float(input("Entre how much fuel want :"))
    total=Liter_price*liter

    if liter > 30:
        discount=5
    elif liter > 20:
        discount=2
    else:
        discount=0
    dis_price=(liter*discount)
    final=total-dis_price


    print(f"\nfuel :{Fuel_type}")
    print(f"{Fuel_type} price is :{Liter_price}")
    print(f"Total fuel bill is :{total}")
    print(f"Total discount is :{dis_price}")
    print(f"Final amount is :{total}-{dis_price} = {final}")

    add=input("\nEntre Yes for next customer\n  No for close petrol pump :").lower()
    if add=="no" or "n":
        break

