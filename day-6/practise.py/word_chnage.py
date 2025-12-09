# with open(r"C:\Users\B A P S\Desktop\python_intern\word_contain.txt") as f:
#     print(f.read())

word="panda"
with open(r"C:\Users\B A P S\Desktop\python_intern\day-6\practise.py\word_contain.txt") as f:
    da=f.read()
dada=da.replace(word,"demon")

with open(r"C:\Users\B A P S\Desktop\python_intern\day-6\practise.py\word_contain.txt","w")as f:
    f.write(dada)
    print(dada)