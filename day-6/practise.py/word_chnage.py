with open(r"C:\Users\B A P S\Desktop\python_intern\day-6\practise.py\jadu1.txt","r") as f:
    da=f.read()
dada=da.replace("panda","Tejaa")

with open(r"C:\Users\B A P S\Desktop\python_intern\day-6\practise.py\jadu1.txt","w+") as f:
    f.write(dada)

  