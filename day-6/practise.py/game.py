import random

with open(r"C:\Users\B A P S\Desktop\python_intern\day-6\practise.py\highscore.txt",)as f:
    score=random.randint(1,100)
    high=f.read()
    if (high!=""):
        high=int(high)
    else:
        high=0

    print(f"Your score :{score}")

    if score>high:
        with open(r"C:\Users\B A P S\Desktop\python_intern\day-6\practise.py\highscore.txt","w") as f:
            f.write(str(score))

# return score