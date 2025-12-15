class Student:
    def __init__(self,name1,age1,std1,sport): # in parameter name delcare are write in
        self.name=name1                #function(age1)
        self.age=age1        # parameter name write in = "age1"
        self.std=std1
        self.sport=sport

    def student_data(self):
        print(f"{self.name} is age is {self.age} and That Student in {self.std} in sport is{self.sport}")


sport_1="Cricket"
sport_2="Tennis"

student_1=Student("Panda",20,9,sport_1)
student_2=Student("Jadu",16,5,sport_2)

print(student_1.__dict__)
print(student_2.__dict__)