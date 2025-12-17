class Person:
    legs=2
    def __init__(self,name):
        self.name=name

p1=Person('krishna')
print(f'Person name is {p1.name} and has {p1.legs} legs')



class Animal:
    legs=4
    def __init__(self,name):
        self.name=name

a1=Animal('Panda')
print(f'Animal name is {a1.name} and has {a1.legs} legs')

print(f'we can print person named {p1.name} from person class and {a1.name } from this class')