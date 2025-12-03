n=int(input("Entre the number :"))

for i in range(1,n+1):
    print(" "*(n-i),end="") # this for write space in pyarmid (5-1)=4 space print on first line
    print("@"*(2*i-1),end="") # this write for @ print i=(1*2)=(2-1)=1 print 1 @ in first line
                              # this same on i=(2*2)=4-1=3 time print @ in second code
    print("")