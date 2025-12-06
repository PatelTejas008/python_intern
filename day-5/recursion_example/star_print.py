def star(m):
    if(m==0):
        return 1
    print("$" * m)
    star(m-1)

star(5)