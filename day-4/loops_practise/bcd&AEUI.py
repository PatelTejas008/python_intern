li=["a","e","o","i","u"]

user=input("Entre the alphabet check :").lower()
if(user.lower() in li):
    print(f"yes {user} is ls")
else:
    print(f"no {user} is not ls")


for i in range(50):
    if(i%2==0):
        print(f"number is even :{i}")
    else:
        print(f"number is odd :{i}")
