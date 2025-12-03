dic={"c1":"Dog",
"c2":"Cat",
"c3":"Monkey",
"c5":"Donkey",
"c4":"Lion", }

# Entre animal name

#if name in
dot=input("Entre unique animal name :").capitalize()
if((dot in dic.values())):   
        print("you are lose the Game")
        print("Entre another animal name")
else:
        print("you are win game")
        print("Entre mind level diffrent ")