word="i am learning the python language for clg project"

user=input("Entre the word check in dictionary :")
if(user in word):
    print(f"Entre the word {user} is in dictioary")
else:
    print(f"{user} word is not in dictionary" )

# many word check 

dic={
    "l1":"python",
    "l2":"html",
    "l3":"java",
    "l4":"js",
    "l5":"css",
    "l6":"node.js",
    "l7":"swift",
    "l8":"php",
    "l10":"c++",
    "l9":"c",
    "l11":"kothlin",
     }

user1=input("Entre the language name :").lower()

if(user in dic.values()):
    print("You are lose the Game")
else:
    print(f"Entre language {user1} is not in dictionary \nYou Win The Game")