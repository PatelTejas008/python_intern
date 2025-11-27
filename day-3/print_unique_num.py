# u1=int(input("Entre number:"))
# u2=int(input("Entre number:"))
# u3=int(input("Entre number:"))   #both code are same 
# u4=int(input("Entre number:"))
# u5=int(input("Entre number:"))
# u6=int(input("Entre number:"))

# set={u1,u2,u3,u4,u5,u6}
# print(set)

num = set()
u1=int(input("Entre number:"))
num.add(u1)
u2=int(input("Entre number:"))
num.add(u2)
u3=int(input("Entre number:"))  # upper code are same result
num.add(u3)
u4=int(input("Entre number:"))
num.add(u4)
u5=int(input("Entre number:"))
num.add(u5)
u6=int(input("Entre number:"))
num.add(u6)

print(num)


print(type(num))

# 18 and 18 string add in set

w=set()
w.add(("int",18))
w.add(("string","18"))
print(w)