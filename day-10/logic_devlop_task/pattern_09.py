n=3
for i in range(n,0,-1):
    print(" " * (n-i) + "$" * (2*i-1))

n=3
for i in range(n,0,-1):
    for k in range(i,n):
        print(" ",end="")
    for a in range(0,i*2-1):
        print("&",end="")
    print()