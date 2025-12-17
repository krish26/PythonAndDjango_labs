class Person:
    fly='flying' #class attribute

    def __init__(self,name,age): #instance attribute
        self.name=name
        self.age=age

    def show_info(self): # method to show instance and class attribute data
        print(f'name :{self.name} , age : {self.age} is {self.fly}')

p1=Person("Agasya",28) # creating 2 objects 
p2=Person("auro" , 30)

#displayig initial values
p1.show_info()
p2.show_info()

p2.fly='Not flying'

#displaying data after class attribute change

p1.show_info()
p2.show_info()



        