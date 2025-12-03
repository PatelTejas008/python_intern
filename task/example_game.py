# dic = {
#     "c1": "dog",
#     "c2": "cat",
#     "c3": "monkey",
#     "c4": "lion",
#     "c5": "donkey"
# }

# # while True:
# dot = input("Enter unique animal name: ").lower()
# # If animal already exists → lose
# if dot in dic.values():
#         print("You lose the game")
#         print("Enter another animal name")
# else:
#         print("You win the game")
#         print("Enter mind-level different name")


# dic = {
#     "c1": "dog",
#     "c2": "cat",
#     "c3": "monkey",
#     "c4": "lion",
#     "c5": "donkey"
# }

# dot = input("Enter unique animal name: ").lower()

# if dot in dic.values():
#     print("You lose the game")
# else:
#     print("You win the game")

dic = {
    "c1": "dog",
    "c2": "cat",
    "c3": "monkey",
    "c4": "lion",
    "c5": "donkey"
}

# try:
dot = input("Enter unique animal name: ").lower()

if dot == "":
        print("You entered an empty name. Please enter a valid animal name.")
elif dot in (v.lower() for v in dic.values()):
        print("You lose the game")
else:
        print("You win the game")
# except KeyboardInterrupt:
#     print("\nInterrupted by user — exiting.")

