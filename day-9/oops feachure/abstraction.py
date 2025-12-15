class Car:
    def __init__(self,compney,model,color,fuel_type):
        self.compney=compney
        self.model=model
        self.color=color
        self.fuel_type=fuel_type


# That part is abstraction in classs......
    def car_detail(self):
        print(f"Car Compney name is :{self.compney}\nCar Model is :{self.model}\nCar Colour is :{self.color}\nThat Car Fuel Type is :{self.fuel_type}\n ")

p="Petrol"
d="Diesel"
c="Cng"
e="Ev"
car1=Car("BMW","M5","Black",p)
car2=Car("Audi","RS e-tron","White",e)
car3=Car("Honda","CIVIC","Silver",p)
car4=Car("Mahindra","Scorpio s11","Black",d)

car1.car_detail()
car2.car_detail()
car3.car_detail()
car4.car_detail()

