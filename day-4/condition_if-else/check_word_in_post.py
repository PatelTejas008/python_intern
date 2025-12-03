hero=["Antman","Superman","Batman","Spiderman","Ironman",""]

name=input("Entre the Hero Name:").capitalize()
print("Your Entred Name:",name)

if(name in hero):
    print("Hero name is in list of hero",name)
else:
    print("Hero name is not in list",name)

     