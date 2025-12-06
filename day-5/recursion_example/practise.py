# def cv(m):
#     if (m<=0):
#         return
#     print(m)
#     cv(m-1)

# cv(5)


#that print 1 to define value print
def bj(j,v):
    if j>v:
        return
    print(j)
    bj(j+1,v) # recall function then two arugument define

bj(1,50)

def sum(a,b):
    print(a+b)
    return(a+b)

sum(1,5)