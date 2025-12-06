 
dic = {
    "c1": "dog",
    "c2": "cat",
    "c3": "monkey",
    "c4": "lion",
    "c5": "donkey"
}


dot = input("Enter unique animal name: ").lower()

if dot == "" or dot == " ":
        print("You entered an empty name. Please enter a valid animal name.")
elif dot in (v.lower() for v in dic.values()):
        print("You lose the game")
else:
        print("You win the game")