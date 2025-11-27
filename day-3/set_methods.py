set={1,3,2,"patel",80.8}
set2={4,5,6,3,2}

set.add(45)
print(set)

nset=set.copy()
print(nset)

print(set2.difference(set))

set2.difference_update(set)
print(set)
print(set2)

set.discard(1)
print(set)

s3={"BMW","Audi","Skoda","Hyundai","land_rover","jaguar","Pagani","Bugati","Rolls_Royls","Dodge(SKT)"}
print(s3.pop())
