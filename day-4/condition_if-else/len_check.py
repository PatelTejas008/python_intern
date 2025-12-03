# your name length check

name=input("Entre tha Your name :")
g=len(name)

if(len(name)>=10):
    print("Please Entre your name in 10 word")
elif(len(name)):
    print(f"Your name is length is{g}")
else:
    print("Your name is not in word please alphabet")
