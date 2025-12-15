#print n to 1 value use recursion
def re(n):
    if(n<=0):
        return
    print(n)
    re(n-1)

n=int(input("Entre the number :"))
re(n)