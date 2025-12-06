def star(m):
    if(m==0):
        return 1
    print("$" * m)
    star(m-1)

star(5)


def add_star(n):
    i=1
    if(i>n):
        return 1
        
    print("@" * n)
    i+=1
    add_star(n+1)

add_star(7)