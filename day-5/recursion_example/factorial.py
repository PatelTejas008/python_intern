def fact(n):
    if  (n<=0):
        return 1
    return n * fact(n-1)

n=int(input("Entre the number find factorial :"))
print(f"The number of {n} factorial is {fact(n)}")