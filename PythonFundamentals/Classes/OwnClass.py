class Bird(): #class

    def __init__(self,name,colour): #constructor and should always have self as param
        self.name=name   #creates an instance attribute
        self.colour=colour

    def show_all(self):  #method inside class should always have self as param
        print('name :  ' ,self.name)
        print('colour : ', self.colour)

b1=Bird('angel','white')
b2=Bird('devil' ,'red')

b1.show_all()
b2.show_all()

