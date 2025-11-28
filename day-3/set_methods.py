s={1,3,2,"patel",80.8}
set2={4,5,6,3,2}

s.add(45)
print(s)
s.remove(1)
print(s)

nset=s.copy()
print(nset)

print(set2.difference(s))

set2.difference_update(s)
print(s)
print(set2)

s.discard(1)
print(s)

s3={"BMW","Audi","Skoda","Hyundai","land_rover","jaguar","Pagani","Bugati","Rolls_Royls","Dodge(SKT)"}
print(s3.pop())
