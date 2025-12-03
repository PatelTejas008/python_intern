year=int(input("Entre the year check leap year or not :"))


if(year % 400 == 0):
    print(f"{year} is Leap Year")
elif(year % 100 == 0):
    print(f"Entre year {year} is not Leap year")
elif(year % 4 == 0):
    print(f"{year} is Leap Year")

else:
    print(f"Entre year {year} is not Leap year")
    
