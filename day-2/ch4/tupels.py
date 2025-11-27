p1=(1,3,2,5,6,"Toxic","nadar","Gogi","Tapu")
p2=("daya","madhvi","komal","babita",4,6,2,1,0)
p3=(4,5,2,3)

mehta=p1+p2#that use for combine 2 tupple in to one tupple
print(mehta)
repet=p2*2 # that use for tuppeks in valu are convert into multi time print
print(repet)

count=p2.count(3) # that use for count value in tupple how many time  

find=p2.index("komal")# that define () value are where index number here
print(find)

#find in tuppel are value is here or not
print("madhvi" in p2)# that say output in true or false

print(len(p2)) # that output is count how many are value store in this name of tupple in ()

print(min(p3))#that use for in tupple find small int/float value not apply on string
print(max(p3))#that use for in tupple find biggest int/float value not apply on string

a,b,c,d=p3
print(a,b,c,d)# that unpacking value one to another 
print(a,b)# that only print 4,5 