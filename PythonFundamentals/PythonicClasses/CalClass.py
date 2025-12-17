class Circle:
    pi=3.14 #class attribute

    def __init__(self,radius):
        self.radius=radius

    def area(self):  #method for cal radius 
        return self.pi*self.radius*self.radius
    
    def update_attribute(self,new_radius):
        self.radius=new_radius

c1=Circle(20)
c2=Circle(10)
c3=Circle(40)

print('area of c1 is : ',c1.area())
print('area of c2 is :' , c2.area())
print('area of c3 is :' , c3.area())

c1.pi=2

print('area of c1 after chnaging value : ',c1.area())

c3.update_attribute(12)
print('area of c3 after chnaging value : ',c3.area())



