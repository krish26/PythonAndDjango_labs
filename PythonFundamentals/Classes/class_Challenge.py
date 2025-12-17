class Bike:
    wheels=2  # obj att
    colour='black'

    def __init__(self,brand):
        self.brand=brand  # instance attr

    def show(self): # method using instance attr
        print(f'The bike is {self.brand} bike ')
    
    def show2(self): # method using class attr
        print(f'it has {self.wheels} wheels and {self.colour} colour')


    def update(self,new_colour): # method to update attributes
        self.colour=new_colour

b1=Bike('honda')
b2=Bike('RE')

b1.show()
b1.show2()
b2.show()
b2.show2()

b2.update('red')

b2.show()
b2.show2()
