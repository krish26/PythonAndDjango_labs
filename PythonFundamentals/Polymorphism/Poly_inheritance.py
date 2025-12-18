class Life:
    def isAlive(self):
        raise NotImplementedError

class Human(Life):
    def isAlive(self):
        return 'Human is alive '
    
class Cat(Life):
    def isAlive(self):
        return 'cat is alive'

class Car:
    def Honk(self):
            return 'car honking'
       
    

print(Human().isAlive())
print(Cat().isAlive())