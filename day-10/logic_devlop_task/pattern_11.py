n=5
for i in range(1,n+1):
    if(i%2==0):
        print((" ") * (n-(n-1)),end="")
        print("@" * n)
    else:
        print("@"*n)



