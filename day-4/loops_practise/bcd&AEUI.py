li=["a","e","o","i","u"]

user=input("Entre the alphabet check :").lower()
if(user.lower() in li):
    print(f"yes {user} is vovels")
else:
    print(f"no {user} is not vovels")


for i in range(50):
    if(i%2==0):
        print(f"number is even :{i}")
    else:
        print(f"number is odd :{i}")
