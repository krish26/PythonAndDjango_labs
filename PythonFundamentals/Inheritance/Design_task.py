class Vehicle:
    wheels=4
    _max_speed=100

    def __init__(self,wheels,_max_speed):
        self.wheels=wheels
        self._max_speed=_max_speed
    
    def start_engine(self):
        print(f'engine is starting and max speed is {self._max_speed} wheels :{self.wheels}')
 

class Car(Vehicle):
    seats=4
    def __init__(self, wheels, _max_speed,seats):
        super().__init__(wheels, _max_speed)
        self.seats=seats

    def start_engine(self):
        print(f'car {super().start_engine()} with {self.seats} seats)')
    
class Bike(Vehicle):
    pedal=2
    def __init__(self, wheels, _max_speed,pedals):
        super().__init__(wheels, _max_speed)
        self.pedals=pedals
    
    def start_engine(self):
        print(f'bike {super().start_engine()} with {self.pedals} pedals') 

v1=Vehicle()
c1=Car(max_speed=180,seats=4)
b1=Bike(max_speed=80,pedals=2)

v1.start_engine()
c1.start_engine()
b1.start_engine()