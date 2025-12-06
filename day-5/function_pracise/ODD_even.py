def odd_even():
    a=int(input("Entre the number find value are odd or EVen :"))
    if(a==0 or a<0):
        if(a==0):
            print(f"Entre number is {a}")
        elif(a<0):
            print(f"Entre number {a} is minus value")
    elif(a%2==0):
        print(f"{a} is Even number")
    elif(a%2!=0):
        print(f"{a} is Odd number")
    
odd_even()