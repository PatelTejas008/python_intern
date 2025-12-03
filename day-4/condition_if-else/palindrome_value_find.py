l1=[1,2,3,2,1]
l2=["RacecaR"]
l3=[1,2,3,4,5,43,3,2,1]

copylist=l1.copy()
copylist.reverse()

copylist2=l2.copy()
copylist2.reverse()

copylist3=l3.copy()
copylist3.reverse()



if(l1==copylist):
    print ("yes that is palidrome")
else:
    print("no that is palidrome")

if(l3==copylist3):
    print ("yes that is palidrome")
else:
    print("no that is palidrome")

if(l2==copylist2):
    print ("yes that is palidrome")
else:
    print("no that is palidrome")
