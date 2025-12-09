f=open(r"C:\Users\B A P S\Desktop\python_intern\day-6\file io\panda.txt","r")

dj=f.readline()

while (dj != "") :
    print(dj)
    print(type(dj))
    dj=f.readline()

f.close()