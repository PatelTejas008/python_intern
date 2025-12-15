def cv(m):
    if (m<=0):
        return
    print(m)
    cv(m-1)

cv(5)
print("\n")


#that print 1 to define value print
def bj(j,v):
    if j>v:
        return
    print(j)
    bj(j+1,v) # recall function then two arugument define

start=(int(input("Entre the number you want to Start value :")))
end=(int(input("Entre the number you want to End value :")))
bj(start,end)

def sum(a,b):
    print(a+b)
    return(a+b)

print("\n")
sum(1,5)