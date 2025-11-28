store:{"table":["a pieace of furniture","list of facts & figure"],
       "cat":"a small animal"}

clas={"python","c++","C","js","java","kothlin"}
print(len(clas))

#entre user subject name and marks store in dictionary

marksheet={}

s1=input("Entre the subject name:")
s2=float(input(f"Entre the marks of {s1}:"))

s3=input("Entre the subject name:")
s4=float(input(f"Entre the marks of {s3}:"))

s5=input("Entre the subject name:")
s6=float(input(f"Entre the marks of {s5}:"))

s7=input("Entre the subject name:")
s8=float(input(f"Entre the Maths marks of{s7} :"))
# print(marksheet.keys[s1]=s2)
# print(marksheet.keys[s3]=s4)
# print(marksheet.keys[s5]=s6)
# print(marksheet.keys[s7]=s8)


marksheet.update({s1:s2})
marksheet.update({s5:s6})
marksheet.update({s3:s4})
marksheet.update({s7:s8})
 
print(marksheet)