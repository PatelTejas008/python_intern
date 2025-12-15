n=6
for i in range(1,n):
    for a in range(1,n-i):
        print(" ",end="")
    for j in range(1,i*2):
        print("$",end="")

    print()

for i in range(n-2,0,-1):  # i (n-2=3,0,-1)
    for a in range(i,n-1):  # a( 3,5-1=4) =(3,4)next (2,4) next (1,4)
        print(" ",end="")
    for j in range(1,i*2):
        print("$",end="")

    print()


