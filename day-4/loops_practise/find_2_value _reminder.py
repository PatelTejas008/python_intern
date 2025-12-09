# just for Example 2 & 3 number to which value remindeer find = 6

re1=int(input("Entre Which number reminder:")) # 
re2=int(input("Entre Which number reminder:"))
a1={}
a1["num1"]=re1
a1["num2"]=re2
print(a1)
num=int(input("Entre number you want reminder:"))

for v in a1.values():
    if(num % v == 0):
        print(f"number is {num} reminder :{v}")
    else:
        print(f"number in not {num} reminder: {v}")