from Animal import Animal

class Elephant(Animal):
    GROUP = "herbivore"

    def eat(self):
        print('Elephant is Eating!!!')
        self.change_energy(5)
    
    
    def sleep(self):
        print('Elephant is Sleeping....')
        if self.energy < 7:
           self.change_energy(3)
        else:
           self.change_energy(1)

class Deer(Animal):
     GROUP = "herbivore"

     def eat(self):
        print('Deer is Eating!!!')
        self.change_energy(5)
    
     def sleep(self):
        print('Deer is Sleeping....')
        if self.energy < 7:
           self.change_energy(3)
        else:
           self.change_energy(1)

class Giraffe(Animal):
     GROUP = "herbivore"

     def eat(self):
        print('Giraffe is Eating!!!')
        self.change_energy(5)
    
     def sleep(self):
        print('Giraffe is Sleeping....')
        if self.energy < 7:
           self.change_energy(3)
        else:
           self.change_energy(1)

