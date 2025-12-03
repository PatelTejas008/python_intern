a=[]
re1=int(input("Entre number you want reminder:"))
re2=int(input("Entre number you want reminder:"))
a.append(re1)
a.append(re2)
num=int(input("Entre number is find reminder:"))
for v in a:
    if(num % v == 0):
        print(f"Entre number {num} is reminder {v}")
    else:
        print(f"Entre number {num} is not reminder {v}")
