user=int(input("Entre number check prime or not :"))

for i in range(2,user):
    if(user%i)== 0:
        print(f"number {user} is not Prime")
        break
else:
    print(f"Entre number {user} is Prime ")