

for j in range(1,6):
    print("2"*j)


n=int(input("Entre the number :"))
for i in range(1,n+1):
    print(" "*(n-i),end="") # this for write space in pyarmid (5-1)=4 space print on first line
    print("@"*(2*i-1),end="") # this write for @ print i=(1*2)=(2-1)=1 print 1 @ in first line
                              # this same on i=(2*2)=4-1=3 time print @ in second code
    print("")

m=int(input("Entre the number:"))
for h in range(1,m+1):
    if(h==1 or h==m):
        print("$"*(m),end="")
    else:
        print("$",end="")
        print(" "*(m-2),end="")
        print("$",end="")
    print("")