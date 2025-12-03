# check 4 number is palidroma or not

num=int(input("Entre the number of check palidroma"))

# That is int value chnage into the string
t=str(num)

# That is revresed the number value
z=t[ : :-1]


if (t==z):
    print("Entre the number is palidrome")
else:
    print("Entre the number is not")



