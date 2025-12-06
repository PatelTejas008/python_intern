#print n to 1 value use recursion
n=6
def re(n):
    if(n<=0):
        return
    print(n)
    re(n-1)

n=int(input("Entre the number :"))
re(n)