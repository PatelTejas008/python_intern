with open(r"C:\Users\B A P S\Desktop\python_intern\day-6\practise.py\jadu1.txt","r")as f:
    l=f.read()
    if(l.find("panda") == -1):
        print("no word is  not write in file")
    else:
        print('yes word is write in file')

    

f=open(r"C:\Users\B A P S\Desktop\python_intern\day-6\practise.py\jadu1.txt")
word=f.read()
if("panda" in word):
    print("Yes Panda word is in Jadu file")
else:
    print("no Panda word is in Jadu file")
f.close()
