class Student:
    def __init__(self,name1,age1,std1): # in parameter name delcare are write in
        self.name=name1                #function(age1)
        self.age=age1        # parameter name write in = "age1"
        self.std=std1


student_1=Student("Panda",20,9)
student_2=Student("Jadu",16,5)

#delete value in students age
print(student_1.__dict__)   # before
del student_1.age              # delete syntax
print(student_1.__dict__)   # after

#delete the object in class 

print(student_1)     # before
del student_1          # delete Object syntax
print(student_1)     # after
