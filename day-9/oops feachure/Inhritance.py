class Car:
    def __init__(self,compney,model,color,fuel_type):
        self.compney=compney
        self.model=model
        self.color=color
        self.fuel_type=fuel_type


# That part is abstraction in classs......
    def car_detail(self):
        print(f"""Car Compney name is :{self.compney} \nCar Model is :{self.model} \nCar Colour is :{self.color}\nThat Car Fuel Type is :{self.fuel_type}""")


p="Petrol"
d="Diesel"
c="Cng"
e="Ev"

class Dealer(Car):
    def __init__(self,compney,model,color,fuel_type,dealer_area):
        super().__init__(compney,model,color,fuel_type)
        self.dealer_area=dealer_area
    
    def dealer_data(self):
        super().car_detail()
        print(f"Dealer area is :{self.dealer_area}")

dealer1=Dealer("Mahindra","Scropio s11","Black",d,"Vastral-382418")

dealer1.dealer_data()
print(dealer1.dealer_area)
       