Maths=int(input("Entre your Maths marks out of 100 :"))
English=int(input("Entre your English marks out of 100 :"))
computer=int(input("Entre your computer marks out of 100 :"))
Hindi=int(input("Entre your Hindi marks out of 100 :"))
Science=int(input("Entre your Science marks out of 100 :"))

Total=(Maths+English+computer+Hindi+Science)
print(Total)
print("per:",(Total/500)*100)
TotalMarks=(Total/500)*100


if(TotalMarks>=95):
    print("A")
elif(TotalMarks>=85):
    print ("B")
elif(TotalMarks>=70):
    print ("c ")
elif(TotalMarks>=60):
    print ("D")
elif(TotalMarks>=45):
    print ("D+")
else:
    print("Fail")
