hero=["Antman","Superman","Batman","Spiderman","Ironman",""]

name=input("Entre the Hero Name:")
print("Your Entred Name:",name)

if(name.capitalize() in hero):
    print("Hero name is in list of hero",name)
else:
    print("Hero name is not in list",name)

     