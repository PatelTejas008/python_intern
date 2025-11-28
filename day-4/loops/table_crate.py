#for loop using table
i=int(input("Entre the number you want Table :"))

for j in range(11):
    if(i>0):
     print(f"{i}X{j}=",i*j)
    else:
        print("Entre invalid number")
        print("Please Entre Natural number")
        break


# while loop using create table

a=0
h=int(input("Entre the number you want table:"))
while(a<=10):
    print(f"{h}X{a}=",h*a)
    a+=1