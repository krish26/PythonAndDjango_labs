from Animal import Animal

class Elephant(Animal):
    GROUP = "herbivore"

    def eat(self):
        print('Elephant is Eating!!!')
        self.change_energy(20)
    
    
    def sleep(self):
        print('Elephant is Sleeping....')
        if self.energy < 30:
           self.change_energy(15)
        else:
           self.change_energy(8)

class Deer(Animal):
     GROUP = "herbivore"

     def eat(self):
        print('Deer is Eating!!!')
        self.change_energy(20)
    
     def sleep(self):
        print('Deer is Sleeping....')
        if self.energy < 30:
           self.change_energy(15)
        else:
           self.change_energy(8)


class Giraffe(Animal):
     GROUP = "herbivore"

     def eat(self):
        print('Giraffe is Eating!!!')
        self.change_energy(20)
    
     def sleep(self):
        print('Giraffe is Sleeping....')
        if self.energy < 30:
           self.change_energy(15)
        else:
           self.change_energy(8)

