TMOC={"Ladish":["komal","madhvi","daya","babita","roshan","anjali"],
      "Gents":["jethlal","Tarak","bhide","popatlal","hathi","iyer"],
       "kids":["Tapu","gogi","goli","sonu","pinku"],
       }

print(TMOC.items())# print all item of dictionary 

print(TMOC.keys())# print just only keys of dictionary
print(TMOC.values())# print just only value of dictionary
# TMOC.update({"kids":"sonalika"})# update of value of dictionary
print(TMOC)

print(TMOC.get("kids"))# define key name and get value show in key
print(TMOC["Gents"]) # that also same work key name define show value
print(TMOC.get("kids3")) # if keys not that show nonee
#print(TMOC["Gents2"])# if keys not that show error  
r=TMOC.pop("Gents") # removed any specific key /value from dic use this
print(r)
print(TMOC)


# nested dictionary

student={"name":"ramesh",
        "subject":{"maths":54,
                  "science":89,
                   "hindi":90}}

print(student) # that print all data of dictionary
x=(student["subject"].popitem()) # that use when nested dictionary use
print(x)
print(student)



