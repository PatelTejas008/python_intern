class Student:
    def __init__(self,name1,age1,std1): # in parameter name delcare are write in
        self.name=name1                #function(age1)
        self.age=age1        # parameter name write in = "age1"
        self.std=std1

    def student_data(self):
        print(f"{self.name} is age is {self.age} and That Student in {self.std}")
Student_1=Student("Panda",16,11)

Student_1.student_data()

#data chnage in stansdard is easy 
print(Student_1.std)  # Before
Student_1.std=12     # modifay
print(Student_1.std)  # after

