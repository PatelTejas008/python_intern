str1="Panda"

sl=str1[2]# that shoe number of alphabet just like in Panda(n) is 2 index
print(sl)


# slicing
str2="TOXIC PANDA"
print(str2[1:4])# that is starting and ending point define
print(str2[1:])# that is only define a staring point till than end string
print(str2[:4])# that is only define ending point till staring the staring 

                 # -5-4-3-2-1
#string work on 2 type PANDA
                     #  01234
print(str2[-5:-2])# that define only (PAN)


# #String function usesss
string="nadar_Panda"
print(string.upper())#that use all string word convert into capital ABCD
print(string.lower())#that use all string word convert into second abcd
print(string.title())#that use all string word in first word capital convert

print(string.endswith("Panda"))#that function use for check ending are complate with () word or not
print(string.capitalize())#that function are use for in string First alphbet to chnage into capitale word
print(string.replace("nadar","Toxic"))#that function use for chnage string value in function only not real string
print(string.find("Panda"))# that define word in string
print(string.count("a"))#that use for in string how many time use ("a") word
print(string[1: :2])#that works like how many step write they define Ex:[starting:ending:gap]
print(string.index("P"))