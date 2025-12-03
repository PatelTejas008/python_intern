# set() use any number reminder find
re1=int(input("Entre Which number reminder:"))
re2=int(input("Entre Which number reminder:"))

a1=set()
#add value in set
a1.add(re1)
a1.add(re2) 

# Entre value you want remider find
num=int(input("Entre number you want reminder:"))

# formulaa=num%re==0
#ex 49%7==0 
for v in a1:
    if(num % v ==0):
        print(f"number is reminder{v}")
    else:
        print(f"number in not reminder{v}")