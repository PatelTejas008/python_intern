# # d=(2,5)
# for i in range(10):
#     # if(i == 2 or i == 5):
#     # if(i ==(2,5)):
#     if(i in (2,5)):
#         continue
#     print(i)

# a=["panda","Tejaa","Toxic","krishna","divy"]

# for p in a:
#     if(p=="Tejaa"):
#         continue
#     print(p)

# print(a)

# # while loop in using continue statment 
# t=0
# while t<=10:
#     if t==5:
#         t+=1  # that use is important
#         continue
#     print(t)
#     t+=1


# #in list use while to find value

# w=(1,3,45,23,68,34,224,89,67,45,89,90,38)

# x=45
# q=0
# while q<len(w):
#     if(w[q]==x):
#         print("Found value is idx",q)


#in list use for to find value

w=(1,3,45,23,68,34,224,89,67,45,89,90,38)

x=45
idx=0
for q in w:
    if(q==x):
        print("Found value is idx",idx)
    idx+=1
else:
    print("yes")